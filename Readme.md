# Phigaro v. 0.1.1a
Phigaro is a scalable command-line tool for predictions phages and prophages from nucleid acid sequences (including metagenomes) and is based on phage genes HMMs and a smoothing window algorithm.

## Requirements
Note that in order to run Phigaro, you need to have MetaGeneMark and HMMER installed.
To install MetaGenemark, download it at http://topaz.gatech.edu/Genemark/license_download.cgi and follow the instructions.
To install HMMER, download it at http://hmmer.org/

## Installation

```
sudo -H python3 setup.py install
```

## Usage

```
phigaro -h                                                                                                                                                                          15:04:32
usage: phigaro [-h] [-f FASTA_FILE] [-c CONFIG] [-v] [-t THREADS]
optional arguments:
  -h, --help            show this help message and exit
  -f FASTA_FILE, --fasta-file FASTA_FILE
                        Assembly scaffolds\contigs or full genomes
  -c CONFIG, --config CONFIG
                        config file
  -v, --verbose
  -t THREADS, --threads THREADS
                        num of threads (default is num of CPUs)
```

Running time depends on the size of your input data and the number of CPUs used.
The mean running time for a fasta file of ???MB is ... minutes.
(c) N.Pryanichnikov, E.Starikova, 2017