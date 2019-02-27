from .html_templates import *
from bs4 import BeautifulSoup

def form_html_document(prophage_data, plots_data, filename_input):    
  
    def form_tbody(data):
        prophage_index = 1
        tbody = BeautifulSoup(features="lxml").new_tag('tbody')
        for scaffold, scaffold_info in data:
            tr = BeautifulSoup(features="lxml").new_tag('tr', **{'class':'scaffold-name'})
            th = BeautifulSoup(features="lxml").new_tag('th', scope="row", colspan="4")
            th.append(scaffold)
            tr.append(th)
            tbody.append(tr)
            for prophage_info in scaffold_info:
                if (prophage_index == 1):
                    prophage_info = [prophage_index]+prophage_info+['active']
                else:
                    prophage_info = [prophage_index]+prophage_info+[''] 
                tbody.append(BeautifulSoup(row.format(*prophage_info), 'html.parser'))
                prophage_index += 1
        return str(tbody)
                
    def form_plots_body(data):
        plots_body = BeautifulSoup(features="lxml")
        for prophage_index, plot in enumerate(data):
            if prophage_index == 0 :
                div = BeautifulSoup(features="lxml").new_tag('div', **{"class": "tab-pane fade show active",
                                                    "id":"phage-%d"%(prophage_index+1)})
                inner_div = BeautifulSoup(features="lxml").new_tag('div', **{"class": "prophage-plot"})
            else:
                div = BeautifulSoup(features="lxml").new_tag('div', **{"class": "tab-pane fade show",
                                                                       "id": "phage-%d" % (prophage_index + 1)})
                inner_div = BeautifulSoup(features="lxml").new_tag('div', **{"class": "prophage-plot", "style":"display:none"})
            inner_div.append(BeautifulSoup(plot, 'html.parser'))
            div.append(inner_div)
            plots_body.append(div)
        return str(plots_body)
    
    def arrange_html_parts(prophage_data, plots_data, filename_input):
        global header, style_css, body_main, body_table, body_plots, row, footer
        header = header.format(filename_input)
        tbody = form_tbody(prophage_data)
        plots_body = form_plots_body(plots_data)
        body_table = body_table.format(tbody)
        body_plots = body_plots.format(plots_body)
        body_main = body_main.format(body_table, body_plots)
        html = header + style_css + body_main + footer
        return html
    
    return arrange_html_parts(prophage_data, plots_data, filename_input)