from builtins import super

from .base import AbstractTask
from Bio import SeqIO
from phigaro.context import Context

class PreprocessTask(AbstractTask):
    task_name = 'input_file'

    def __init__(self, input):
        super().__init__()
        self.input = input
        self.context = Context.instance()

    def check_fastafile(self):
        def get_users_answer(question):
            yes = ['yes', 'y']
            no = ['no', 'n']
            try:
                input_ = raw_input
            except NameError:
                input_ = input
            prompt_str = "%s %s " % (question, "[Y/n]")
            while True:
                choice = input_(prompt_str).lower()
                if (not choice) or (choice in yes):
                    return True
                if choice in no:
                    return False

        sequences_to_delete = []
        records_to_save = []
        for record in SeqIO.parse(self.input, "fasta"):
            if len(record) < 20000:
                sequences_to_delete.append(record.id)
            else:
                self.context.scaffolds_info[record.id] = len(record)
                records_to_save.append(record)
        SeqIO.write(records_to_save, self.output(), "fasta")
        del records_to_save

        if not self.config['phigaro']['delete_shorts']:
            if len(sequences_to_delete) > 0:
                print(
                    'Error! Your fasta file contains at least one sequence length < 20000.  The short sequences are: ')
                print('\n'.join(sequences_to_delete))
                if not get_users_answer('Do you want to start Phigaro without these sequences?'):
                    self.clean()
                    exit(1)

    def output(self):
        return self.file('{}.fasta'.format(self.sample))

    def run(self):
        self.check_fastafile()