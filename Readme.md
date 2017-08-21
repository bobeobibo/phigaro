# Phigaro v. 0.1.1a
Phigaro is a command-line tool for predictions phages and prophages from nucleid acid sequences (including metagenomes) and is based on phage genes HMMs (pVOG) and a smoothing window algorithm.

## Requirements
Note that in order to run Phigaro, you need to have MetaGeneMark and HMMER installed.
To install MetaGenemark, download it at http://topaz.gatech.edu/Genemark/license_download.cgi and follow the instructions.
To install HMMER, download it at http://hmmer.org/
Also note that you need `locate` to successfully run setup. It is pre-installed in the latest Ubuntu distributions, but in case you don't have it, please run `sudo apt-get install locate`, it is a very useful tool.

## Installation

```
sudo -H python3 setup.py install
```
then create a config file with:
```
phigaro-setup
```
It may take some time, since we are downloading the database

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

## Output
The output looks li

## Modus operandi
ORFs and corresponging proteins are predicted from the input .fasta file using MetaGeneMark. Phage genes are predicted with pVOG Hidden Markov Models that can be downloaded stand-alone from http://dmk-brain.ecn.uiowa.edu/pVOGs/. Each contig is represented as a sequence of phage and non-phage genes. A smoothing window algorithm determines regions with high density of phage genes and prophage boundaries.

In case of any questions regarding installing and running Phigaro please adress estarikova@rcpcm.org

(c) N.Pryanichnikov, E.Starikova, 2017
