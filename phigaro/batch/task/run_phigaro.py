import csv
from builtins import super

from phigaro.data import read_prodigal_output, read_hmmer_output, hmmer_res_to_npn, hmmer_res_to_gc, Gene, define_taxonomy
from phigaro.finder.v2 import V2Finder
from phigaro import const
from .base import AbstractTask
from .prodigal import ProdigalTask
from .hmmer import HmmerTask
import os

from phigaro.to_html.preprocess import plot_html, form_sequence, if_transposable
from phigaro.to_html.html_formation import form_html_document

class RunPhigaroTask(AbstractTask):
    task_name = 'run_phigaro'

    def __init__(self, hmmer_task, prodigal_task):
        """
        :type hmmer_task: HmmerTask
        :type prodigal_task: ProdigalTask
        """
        super().__init__()
        self.hmmer_task = hmmer_task
        self.prodigal_task = prodigal_task

    def _prepare(self):
        self.finder = V2Finder(
            window_len=self.config['phigaro']['window_len'],
            threshold_min=self.config['phigaro']['threshold_min'],
            threshold_max=self.config['phigaro']['threshold_max'],
        )
        self._print_vogs = self.config['phigaro'].get('print_vogs', False)
        self._filename = self.config['phigaro'].get('filename', False)
        self._no_html = self.config['phigaro'].get('no_html', False)
        self._not_open = self.config['phigaro'].get('not_open', False)
        self._output = self.config['phigaro'].get('output', False)
        self._uuid = self.config['phigaro'].get('uuid', False)

    def output(self):
        return self.file('{}.tsv'.format(self.sample))

    def run(self):
        max_evalue = self.config['hmmer']['e_value_threshold']
        penalty_black = self.config['phigaro']['penalty_black']
        penalty_white = self.config['phigaro']['penalty_white']

        pvogs_black_list = const.DEFAULT_BLACK_LIST
        pvogs_white_list = const.DEFAULT_WHITE_LIST

        scaffold_set = read_prodigal_output(self.prodigal_task.output())
        hmmer_result = read_hmmer_output(self.hmmer_task.output())

        with open(self.output(), 'w') as of:
            writer = csv.writer(of, delimiter='\t')

            if self._print_vogs:
                writer.writerow(('scaffold', 'begin', 'end', 'transposable', 'taxonomy', 'vog'))
            else:
                writer.writerow(('scaffold', 'begin', 'end', 'transposable', 'taxonomy'))

            plotly_plots = []
            phage_info = []
            transposables_status = []
            phage_num = 0
            for scaffold in scaffold_set:
                phage_info.append([scaffold.name, []])
                genes = list(scaffold)  # type: list[Gene]
                npn = hmmer_res_to_npn(scaffold, hmmer_result, max_evalue=max_evalue,
                                       penalty_black = penalty_black, penalty_white = penalty_white,
                                       pvogs_black_list = pvogs_black_list, pvogs_white_list = pvogs_white_list)
                gc = hmmer_res_to_gc(scaffold, hmmer_result, max_evalue=max_evalue)

                phages = self.finder.find_phages(npn, gc)
                for phage in phages:
                    phage_num += 1
                    begin = genes[phage.begin].begin
                    end = genes[phage.end].end
                    hmmer_records = [
                        hmmer_result.min_record(hmmer_result.get_records(scaffold.name, gene.name))
                        for gene in genes[phage.begin: phage.end]
                    ]
                    hmmer_pvogs_records = (
                        record.vog_name
                        for record in hmmer_records
                        if record and record.evalue <= max_evalue
                    )
                    pvogs_records_str = ', '.join(hmmer_pvogs_records)
                    taxonomy = define_taxonomy(pvogs_records_str)
                    hmmer_records = [
                        record
                        for record in hmmer_records
                        if record and record.evalue <= max_evalue
                    ]
                    transposable = if_transposable(hmmer_records)
                    if self._print_vogs:
                        writer.writerow((scaffold.name, begin, end, transposable, taxonomy,  pvogs_records_str))
                    else:
                        writer.writerow((scaffold.name, begin, end, transposable, taxonomy))

                    sequence = form_sequence(self._filename, '%s_prophage_%d' % (scaffold.name, phage_num), begin, end, scaffold.name)
                    transposables_status.append(transposable)
                    the_phage_info = [begin, end, taxonomy, sequence, pvogs_records_str]
                    phage_info[-1][1].append(the_phage_info)
                    if (not self._no_html) and (self._output):
                        plotly_plots.append(plot_html(hmmer_records, begin, end))
                phage_info = phage_info if len(phage_info[-1][1]) > 0 else phage_info[:-1]
            if (len(phage_info) > 0) and (not self._no_html) and (self._output):
                html = form_html_document(phage_info, transposables_status, plotly_plots, self._filename, self._uuid)
                with open(self._output+'.html', 'w') as f:
                    f.write(html)
                if not self._not_open:
                    os.system('xdg-open '+self._output+'.html'+' > /dev/null 2>/dev/null')