import numpy as np
from plotly import tools
from plotly.graph_objs import Bar
import plotly.offline as py

from phigaro.finder.v2 import calc_scores

def _make_coords_colors(data_len, real_phage_coords):
    colors = np.zeros(data_len)
    for begin, end in real_phage_coords:
        for i in range(begin, end + 1):
            colors[i] = 1
    return colors


def plot_scores(scores, title, real_phage_coords=None):
    indices = np.arange(len(scores))

    colors = None
    if real_phage_coords is not None:
        colors = _make_coords_colors(len(scores), real_phage_coords)
    data = Bar(
        x=indices,
        y=scores + 0.1,
        name=title,
        marker=dict(
            color=colors,
        )
    )

    return data


def plot_phage(phage, title):
    ind = np.arange(len(phage))
    int_phage = [c + .1 for c in phage]
    data = Bar(
        x=ind,
        y=int_phage,
        marker=dict(
            color='black',
        ),
        name=title
    )
    return data


def _make_rects(coords, ymin, ymax, fillcolor, opacity):
    return [
        dict(
            type='rect',
            xref='x',
            yref='y',
            x0=x_begin,
            y0=ymin,
            x1=x_end,
            y1=ymax,
            fillcolor=fillcolor,
            opacity=opacity,
            line={'width': 0}
        )
        for (x_begin, x_end) in coords
        ]


def plot_scores_and_phage(phage, window_len, score_func=None, scan_func=None, real_phage_coords=None):
    score_func = score_func or score_tri
    fig = tools.make_subplots(rows=2, cols=1, shared_xaxes=True)
    title = 'Scores: window: {}'.format(window_len)
    scores = np.array(calc_scores(phage, window_len, score_func))

    ranges = []
    if scan_func is not None:
        ranges = scan_func(scores)

    score_fig = plot_scores(scores, title, real_phage_coords=None)
    phage_fig = plot_phage(phage, 'Phage')

    fig.append_trace(score_fig, 1, 1)
    fig.append_trace(phage_fig, 2, 1)

    ymax = window_len / 2
    if real_phage_coords is not None or ranges:
        fig['layout'].update(dict(
            shapes=_make_rects(ranges, ymax, 'rgb(50, 171, 96)', 0.5) + _make_rects(real_phage_coords or [], ymax, '#ff0000', 0.5)

        ))

    py.iplot(fig)


def plot_scores_and_phage2(phage, scores, found_phage_coords, real_phage_coords=None, filename='filename'):
    # real_phage_coords = real_phage_coords or []
    fig = tools.make_subplots(rows=2, cols=1, shared_xaxes=True)
    title = 'Scores'

    score_fig = plot_scores(scores, title, real_phage_coords=None)
    phage_fig = plot_phage(phage, 'Phage')

    fig.append_trace(score_fig, 1, 1)
    fig.append_trace(phage_fig, 2, 1)

    ymax = max(scores)
    # print(len(real_phage_coords), len(found_phage_coords))
    if (len(real_phage_coords) + len(found_phage_coords)) != 0:
        # print('got real coords')
        fig['layout'].update(dict(
            shapes=_make_rects(found_phage_coords, ymax * 0.5, ymax * 0.75, '#0000ff', 0.5) + \
                   _make_rects(real_phage_coords, ymax * 0.75, ymax, '#aaaa00', 0.5)

        ))

    py.plot(fig, filename=filename+'.html')
