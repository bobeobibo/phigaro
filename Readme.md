# Phigaro v. 0.2.0
Phigaro is a command-line tool for predictions phages and prophages from nucleid acid sequences (including metagenomes) and is based on phage genes HMMs (pVOG) and a smoothing window algorithm.

## Requirements
Note that in order to run Phigaro, you need to have Prodigal and HMMER installed.
To install Prodigal, download it at https://github.com/hyattpd/Prodigal/wiki/installation and follow the instructions.
To install HMMER, download it at http://hmmer.org/
Also note that you need `locate` to successfully run setup. It is pre-installed in the latest Ubuntu distributions, but in case you don't have it, please run `sudo apt-get install locate`, it is a very useful tool.

## Installation

```
sudo -H pip3 install phigaro
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
  -o, --output OUTPUT 
                        output file, not required, default is stdout
  -p, --print-vogs
                        print phage vogs for each region
  --no-html 
                        do not generate output html file
  --not-open 
                        do not open automatically html file
```
Running time depends on the size of your input data and the number of CPUs used.
The approximate running time for a metagenomic assembly file of 150MB is about 20 minutes.

## Output
The output is in .bed format

## Modus operandi
ORFs and corresponging proteins are predicted from the input .fasta file using Prodigal. Phage genes are predicted with pVOG Hidden Markov Models that can be downloaded stand-alone from http://dmk-brain.ecn.uiowa.edu/pVOGs/. Each contig is represented as a sequence of phage and non-phage genes. A smoothing window algorithm determines regions with high density of phage genes and prophage boundaries.

In case of any questions regarding installing and running Phigaro please adress estarikova@rcpcm.org

(c) E.Starikova, P. Tikhonova, N.Pryanichnikov, 2019
