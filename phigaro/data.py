import csv
import re
from collections import OrderedDict, defaultdict, Iterable
from itertools import groupby

from phigaro.misc.ranges import first

INFINITY = float('inf')


def read_npn(filename, sep=None, as_dict=True):
    sep = sep or ' '
    with open(filename) as f:
        reader = csv.reader(f, delimiter=sep)
        if as_dict:
            return dict(reader)
        else:
            return reader


def read_coords(filename, sep=None):
    sep = sep or '\t'
    with open(filename) as f:
        reader = csv.reader(f, delimiter=sep)
        res = {}
        for phage, group in groupby(reader, key=lambda x: x[0]):
            res[phage] = sorted((
                (int(begin), int(end))
                for _, begin, end in group
            ), key=lambda x: x[0])
    return res


def convert_npn(phage, ph_sym):
    return [
        int(c == ph_sym)
        for c in phage
    ]


def hmmer_res_to_npn(scaffold, hmmer_result, max_evalue, penalty_black, pvogs_black_list):
    # type: (Scaffold, HmmerResult, float)->list[int]
    ordered_records_it = (
        HmmerResult.min_record(hmmer_result.get_records(scaffold.name, gene.name))
        for gene in scaffold
    )

    return [
        0
        if not record or record.evalue > max_evalue
        else 1 - penalty_black if record.vog_name in pvogs_black_list
        else 1
        for record in ordered_records_it
    ]


class Gene(object):
    def __init__(self, name, begin, end, scaffold=None):
        # type: (str, int, int, Scaffold|None)->Gene
        self.name = name
        self.begin = begin
        self.end = end
        self.scaffold = scaffold


class Scaffold(object):
    def __init__(self, name, genes):
        # type: (str, list[Gene])->Scaffold
        self.name = name
        self._genes_map = OrderedDict()

        for gene in sorted(genes, key=lambda g: g.begin):
            gene.scaffold = self
            self._genes_map[gene.name] = gene

    def __iter__(self):
        # type: ()->Iterable[Gene]
        return iter(self._genes_map.values())

    def get_gene(self, gene_name):
        # type: (str)->Gene
        return self._genes_map[gene_name]


class ScaffoldSet(object):
    def __init__(self, scaffolds):
        # type: (list[Scaffold])->ScaffoldSet
        self._scaffolds_map = {
            scaffold.name: scaffold
            for scaffold in scaffolds
        }

    def get_scaffold(self, scaffold_name):
        # type: (str)->Scaffold
        return self._scaffolds_map[scaffold_name]

    def __iter__(self):
        return iter(self._scaffolds_map.values())


class HmmerRecord(object):
    def __init__(self, scaffold_name, gene_name, vog_name, evalue):
        # type: (str, str, str, float)->HmmerRecord
        self.scaffold_name = scaffold_name
        self.gene_name = gene_name
        self.vog_name = vog_name
        self.evalue = evalue


class HmmerResult(object):
    def __init__(self, hmmer_records):
        # type: (Iterable[HmmerRecord])->HmmerResult
        self._scaffolds_map = defaultdict(lambda: defaultdict(list))  # type: dict[str, dict[str, list[HmmerRecord]]]
        for hmmer_record in hmmer_records:
            self._add_record(hmmer_record)

    def _add_record(self, hmmer_record):
        # type: (HmmerRecord)->None
        scaffold_records = self._scaffolds_map[hmmer_record.scaffold_name]
        scaffold_records[hmmer_record.gene_name].append(hmmer_record)

    def get_records(self, scaffold_name, gene_name):
        # type: (str, str)->list[HmmerRecord]
        return self._scaffolds_map[scaffold_name].get(gene_name, [])

    @staticmethod
    def min_record(records):
        # type: (list[HmmerRecord])->HmmerRecord|None
        if not records:
            return None
        return min(records, key=lambda r: r.evalue)


def read_hmmer_output(file_path):
    # type: (str)->HmmerResult

    def parse_line(line):
        # type: (str)->HmmerRecord
        tokens = re.split(r'\s+', line)

        return HmmerRecord(
            scaffold_name='_'.join(tokens[0].split('_')[:-1]),
            gene_name=tokens[0].split('_')[-1],
            vog_name=tokens[2],
            evalue=float(tokens[4])
        )

    with open(file_path) as f:
        lines_it = (
            parse_line(line.strip())
            for line in f
            if not line.startswith('#') and line.strip()
        )

        hmm_res = HmmerResult(lines_it)

        return hmm_res


def read_prodigal_output(file_name):
    # type: (str)->ScaffoldSet

    def extract_coords_and_name(gene_str):
        # type: (str)->Gene

        tokens = gene_str.split(' # ')
        return Gene(
            name=tokens[0],
            begin=int(tokens[1]),
            end=int(tokens[2])
        )

    def parse_gene_records(gene_records):
        # type: (list[str])->list[Gene]
        return [
            extract_coords_and_name(gene_str)
            for _, gene_str in gene_records
        ]

    with open(file_name) as f:
        genes_scaffold_recs = (
            ['_'.join(line.strip().split(' # ', 1)[0].split('_')[:-1]),
             line.strip().split(' # ', 1)[0].split('_')[-1]+' # '+line.strip().split(' # ', 1)[1]]
            for line in f
            if line.startswith('>')
        )

        scaffolds = [
            Scaffold(
                name=scaffold_name[1:],
                genes=parse_gene_records(gene_records)
            )
            for scaffold_name, gene_records in groupby(genes_scaffold_recs, key=first)
        ]

        return ScaffoldSet(scaffolds=scaffolds)

