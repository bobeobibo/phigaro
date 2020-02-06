import csv
from builtins import super

from phigaro.data import read_prodigal_output, read_hmmer_output, hmmer_res_to_npn, hmmer_res_to_gc, Gene, define_taxonomy
from phigaro.finder.v2 import V2Finder
from phigaro import const
from .base import AbstractTask
from .prodigal import ProdigalTask
from .hmmer import HmmerTask
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from phigaro.to_html.preprocess import plot_html, form_sequence, if_transposable
from phigaro.to_html.html_formation import form_html_document
from phigaro.context import Context
import numpy as np

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
        self.mode = self.config['phigaro']['mode']
        self.finder = V2Finder(
            window_len=self.config['phigaro']['window_len'],
            threshold_min=self.config['phigaro']['threshold_min_%s'%self.mode],
            threshold_max=self.config['phigaro']['threshold_max_%s'%self.mode],
            mode=self.mode
        )
        self._print_vogs = self.config['phigaro'].get('print_vogs', False)
        self._filename = self.config['phigaro'].get('filename', False)
        self._no_html = self.config['phigaro'].get('no_html', False)
        self._not_open = self.config['phigaro'].get('not_open', False)
        self._save_fasta = self.config['phigaro'].get('save_fasta', False)
        self._output = self.config['phigaro'].get('output', False)
        self._uuid = self.config['phigaro'].get('uuid', False)
        self.context = Context.instance()

    def output(self):
        return self.file('{}.tsv'.format(self.sample))

    def run(self):
        max_evalue = self.config['hmmer']['e_value_threshold']
        penalty_black = self.config['phigaro']['penalty_black']
        penalty_white = self.config['phigaro']['penalty_white']
        gff = self.config['phigaro']['gff']
        bed = self.config['phigaro']['bed']
        mean_gc = self.config['phigaro']['mean_gc']

        pvogs_black_list = const.DEFAULT_BLACK_LIST
        pvogs_white_list = const.DEFAULT_WHITE_LIST

        scaffold_set = read_prodigal_output(self.prodigal_task.output())
        hmmer_result = read_hmmer_output(self.hmmer_task.output())

        gff_base = ['##gff-version 3.2.1']
        gff_scaffold = []
        gff_prophage = []
        gff_gene = []
        bed_prophage = []
        bed_gene = []

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
                if gff:
                    gff_scaffold.append('##sequence-region %s 1 %d'%(scaffold.name, self.context.scaffolds_info[scaffold.name]))
                phage_info.append([scaffold.name, []])
                genes = list(scaffold)  # type: list[Gene]
                npn = hmmer_res_to_npn(scaffold, hmmer_result, max_evalue=max_evalue,
                                       penalty_black = penalty_black, penalty_white = penalty_white,
                                       pvogs_black_list = pvogs_black_list, pvogs_white_list = pvogs_white_list)
                gc = hmmer_res_to_gc(scaffold, hmmer_result, max_evalue=max_evalue)
                if self.mode == 'abs':
                    gc = np.array(gc)
                    gc = np.absolute(gc - mean_gc) + mean_gc
                    gc[gc == np.absolute(0 - mean_gc) + mean_gc] = 0
                phages = self.finder.find_phages(npn, gc)
                for phage in phages:
                    phage_num += 1
                    begin = genes[phage.begin].begin
                    end = genes[phage.end].end
                    phage_genes = genes[phage.begin:(phage.end+1)]
                    if gff:
                        gff_prophage.append('\t'.join([scaffold.name, '.', 'prophage',
                                                       str(begin+1), str(end+1),
                                                       '.', '.', '.',
                                                       'ID=prophage%d'%phage_num]))
                    if bed:
                        bed_prophage.append('\t'.join([scaffold.name,
                                                       str(begin), str(end),
                                                       'prophage%d' % phage_num,
                                                       '.', '.']))
                    hmmer_records = [
                        hmmer_result.min_record(hmmer_result.get_records(scaffold.name, gene.name))
                        for gene in genes[phage.begin: phage.end]
                    ]
                    if gff or bed:
                        for record in phage_genes:
                            hmmer_record = hmmer_result.min_record(hmmer_result.get_records(scaffold.name, record.name))
                            pvog = '.' if hmmer_record is None else hmmer_record.vog_name
                            evalue = '.' if hmmer_record is None else hmmer_record.evalue
                            if gff:
                                gff_gene.append('\t'.join([scaffold.name, '.', 'gene',
                                                       str(record.begin+1), str(record.end+1),
                                                       str(evalue), '+' if record.strand>0 else '-', '.',
                                                       'ID=gene%s;Parent=prophage%d;pvog=%s'%(record.name, phage_num, pvog)]))
                            if bed:
                                bed_gene.append('\t'.join([scaffold.name,
                                                           str(record.begin), str(record.end+1),
                                                           'gene%s' % (record.name),
                                                           str(evalue), '+' if record.strand > 0 else '-']))

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

                    sequence, record = form_sequence(self._filename, '%s_prophage_%d' % (scaffold.name, phage_num), begin, end, scaffold.name)
                    transposables_status.append(transposable)
                    the_phage_info = [begin, end, taxonomy, sequence, pvogs_records_str]
                    phage_info[-1][1].append(the_phage_info)
                    if self._save_fasta:
                        with open(self._output+'.fasta', 'a') as f:
                            SeqIO.write(SeqRecord(record, id='%s_prophage_%d' % (scaffold.name, phage_num),
                                                  description='%s_prophage_%d' % (scaffold.name, phage_num)), f, "fasta")
                    if (not self._no_html) and (self._output):
                        plotly_plots.append(plot_html(hmmer_records, begin, end))
                phage_info = phage_info if len(phage_info[-1][1]) > 0 else phage_info[:-1]

            if gff:
                with open(self._output+'.gff3', 'w') as f:
                    f.write('\n'.join(gff_base+gff_scaffold+gff_prophage+gff_gene))
            if bed:
                with open(self._output+'.bed', 'w') as f:
                    f.write('\n'.join(gff_base+bed_prophage+bed_gene))

            if (len(phage_info) > 0) and (not self._no_html) and (self._output):
                html = form_html_document(phage_info, transposables_status, plotly_plots, self._filename, self._uuid)
                with open(self._output+'.html', 'w') as f:
                    f.write(html)
                if not self._not_open:
                    os.system('xdg-open '+self._output+'.html'+' > /dev/null 2>/dev/null')