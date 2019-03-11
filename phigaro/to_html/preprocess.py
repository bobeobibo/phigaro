import pickle
import plotly.graph_objs as go
from plotly.offline import plot
import numpy as np
import os
from Bio import SeqIO

pvogs_groups = ['Lysis', 'Integration', 'Terminase', 'Replication',
                                'Coat', 'Baseplate', 'Tail', 'Assembly','Portal','Other (structural)','Other']
cmap = [(31,119,180), (255,127,14), (44,160,44), (214,39,40),
        (188,189,34), (23,190,207), (148,103,189), (227,119,194),
        (0,0,128),(32,50,50),(127,127,127)]
colors = {group:cmap[i] for i, group in enumerate(pvogs_groups)}

with open(os.path.dirname(os.path.abspath(__file__))+'/pvogs_annotations.pickle', 'rb') as f:
    annotations = pickle.load(f)

def form_arrow(begin, end, nonreverse, width):
    '''
    :param begin: int (of gene)
    :param end: int (of gene)
    :param nonreverse: boolean
    :param width:
    :return: tuple of tuples (arrow coords)
    '''
    k = 0.05
    height = 0.9 if width < 0.4 else 1
    width = width if width > 0.6 else 0.6
    if nonreverse:
        return ((begin, 1-width*k), (begin, 1+width*k), (begin+0.6*(end-begin), 1+width*k),
                (begin+0.6*(end-begin), 1+1.8*height*k), (end, 1),
                (begin+0.6*(end-begin), 1-1.8*height*k), (begin+0.6*(end-begin), 1-width*k))
    else:
        return ((end, 1-width*k), (end, 1+width*k), (end-0.4*(end-begin), 1+width*k),
                (end-0.4*(end-begin), 1+1.8*height*k), (begin, 1),
                (end-0.4*(end-begin), 1-1.8*height*k), (end-0.4*(end-begin), 1-width*k))

def plot_html(records, prophage_begin, prophage_end):
    '''
    :param records: list of Gene
    :return: html_plot
    '''
    def _plotly_to_html_(prophage_begin, prophage_end, func_groups, widths, coords, arrow_coords):
        global colors, pvogs_groups
        traces0 = [go.Scatter(
            x=[prophage_begin],
            y=[100],
            mode='markers',
            opacity=1,
            hoverinfo='none',
            marker=dict(
                size=10,
                color='rgba(%.5f, %.5f, %.5f, 0.8)' % colors[group],
            ),
            name=group
        )
        for group in pvogs_groups if group in func_groups.keys()
        ] + [go.Scatter(
            x=np.array(coords)[elements],
            y=[1] * len(elements),
            text=np.array(records_info)[elements],
            hoverinfo='text',
            mode='markers',
            marker=dict(
                size=90 * np.array(widths)[elements],
                color='rgba(%.5f, %.5f, %.5f, 1)' % colors[group],
                opacity=0
            ),
            showlegend=False
        )
        for group, elements in func_groups.items()]
        trace1 = [go.Scatter(
            x=[prophage_begin, prophage_end],
            y=[1, 1],
            mode='lines',
            line=dict(
                color='rgba(116,116,116, 0.5)',
                width=1
            ),
            hoverinfo='none',
            showlegend=False
        )]
        layout = {
            'yaxis': dict(
                range=[-.5, 2.5],
                showgrid=False,
                zeroline=False,
                showline=False,
                ticks='',
                showticklabels=False
            ),
            'xaxis': dict(
                title='Nucleotide Number'
            ),
            'shapes': [
                {
                    'type': 'path',
                    'path': 'M ' + ' '.join(['L {:.5f},{:.5f}'.format(*arrow_point) for arrow_point in arrow])[1:] + ' Z',
                    'fillcolor': 'rgba(%.5f, %.5f, %.5f, 1)' % colors[group],  # 'rgba(44, 160, 101, 0.5)'
                    'opacity': 0.7,
                    'line': {
                        'color': 'rgba(%.5f, %.5f, %.5f, 0.7)' % colors[group],
                    },
                }
                for group, elements in func_groups.items() for arrow in np.array(arrow_coords)[elements]]
        }
        data = traces0 + trace1
        fig = {
            'data': data,
            'layout': layout,
        }
        return fig

    pvogs = []
    widths = []
    coords = []
    arrow_coords = []
    records_info = []
    func_groups = {}
    for i, record in enumerate(records):
        pvogs.append(record.vog_name)
        widths.append(record.end - record.begin)
        coords.append(record.begin + (record.end - record.begin) / 2.0)
        arrow_coords.append((record.begin, record.end, (record.strand + 1) / 2))
        records_info.append('%s<br>%d-%d<br>gc_cont = %s' % (record.vog_name, record.begin, record.end, record.gc_cont))
        group = annotations.loc[record.vog_name.strip()].group if record.vog_name.strip() in annotations.index else 'Other'
        if group in func_groups.keys():
            func_groups[group].append(i)
        else:
            func_groups[group] = [i]
    widths = 1.0 * (np.array(widths) - min(widths)) / max(widths) + 0.1
    arrow_coords = [form_arrow(*info, width=width) for info, width in zip(arrow_coords, widths)]
    plotly_fig = _plotly_to_html_(prophage_begin, prophage_end, func_groups, widths, coords, arrow_coords)
    return plot(plotly_fig, include_plotlyjs=False, filename='gene_map.html', output_type='div')

def form_sequence(fasta_file, fasta_name, prophage_begin, prophage_end, scaffold_name):
    for record in SeqIO.parse(fasta_file, "fasta"):
        if record.id.strip() == scaffold_name.strip():
            sequence = record.seq[prophage_begin:(prophage_end + 1)]
            ins_ind = 77
            while ins_ind < len(sequence):
                sequence = sequence[:ins_ind] + '%0A' + sequence[ins_ind:]
                ins_ind += 80
            sequence = '%' + '3E%s' % fasta_name + '%' + '0A%s' % sequence
            return sequence

def if_transposable(records):
    status = False
    for record in records:
        group = annotations.loc[record.vog_name.strip()].group if record.vog_name.strip() in annotations.index else 'Other'
        if (group == 'Integration') & status:
            return True
        elif (group == 'Integration'):
            status = True
        elif (group != 'Integration') & (group != 'Other'):
            status = False
    return False
