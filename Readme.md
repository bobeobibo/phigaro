# Phigaro v 0.2.1.7
Phigaro is a command-line tool for predicting and annotating phages and prophages from nucleid acid sequences (including metagenome assemblies) and is based on identifying phage genes via pVOG profile HMMs and a smoothing window algorithm.

## Requirements
In order to run Phigaro, you need to have Prodigal and HMMER installed.
To install Prodigal, download it at https://github.com/hyattpd/Prodigal/wiki/installation and follow the instructions.
To install HMMER, download it at http://hmmer.org/.
You also need `locate`. It is pre-installed in the latest Ubuntu distributions, but in case you don't have it, please run `sudo apt-get install locate`.

## Installation

```
sudo -H pip3 install phigaro
```
then create a config file with:
```
phigaro-setup
```
It may take some time, since you are downloading the databases.

## Usage

```
phigaro -h                                                                                                                                                                          15:04:32
usage: phigaro [-h] [-V] -f FASTA_FILE [-c CONFIG] [-p] [-e EXTENSION [EXTENSION ...]] [-o OUTPUT] [--not-open] [-t THREADS]

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
                        output filename for html and txt outputs. Required by default, but not required for stdout only output
  -p, --print-vogs
                        print phage vogs for each region
  --no-html 
                        do not generate output html file
  --not-open 
                        do not open automatically html file
  -e, --extension
                        type of the output: html, txt or stdout. Default is html. You can specify several file formats with a space as a separator. Example: -e txt html stdout
  --not-open
                        do not open html file automatically, if html output type is specified
```
Running time depends on the size of your input data and the number of CPUs used.
The running time for a metagenomic assembly file of 150MB is about 20 minutes.

## Output
The output can be annotated prophage genome maps (html) or tabular format (text or stdout).

## Test data
Test data is available in `test_data` folder. 
In order to run Phigaro on test data, enter the following command from your Phigaro folder:

```
phigaro -f test_data/Bacillus_anthracis_str_ames.fna -o test_data/Bacillus_anthracis_str_ames.phg -p --not-open
```
This command generates `Bacillus_anthracis_str_ames.phg` and `Bacillus_anthracis_str_ames.phg.html` files in `test_data` folder.
If output file is not specified with `-o`, the following output is generated:
```
scaffold        begin   end     taxonomy
NC_003997.3     451613  457261  Siphoviridae
NC_003997.3     460328  482139  Siphoviridae
NC_003997.3     3460450 3482979 Siphoviridae
NC_003997.3     3495703 3505502 Siphoviridae
NC_003997.3     3749518 3776811 Siphoviridae
NC_003997.3     3779698 3784171 Siphoviridae
```

## Methods overview
Open-reading frames (i.e. proteins) are predicted from the input FASTA file using Prodigal. Phage genes are annotated with prokaryotic viral orthologous groups (pVOGs) profile Hidden Markov Models (HMMs), which can be downloaded stand-alone from http://dmk-brain.ecn.uiowa.edu/pVOGs/. Each contig is represented as a sequence of phage and non-phage genes. A smoothing window algorithm (a triangular window function) determines regions with a high density of phage genes and therefore the prophage regions and boundaries, considering the pVOG annotations and the GC content.

## Known issues
Phigaro is tested on Linux systems. For MacOS, you may need to add the following softlink `ln -s /usr/libexec/locate.updatedb /usr/local/bin/updated` and run `brew install wget`. Currently, root permissions are required for the installation. If you encounter any issues while running Phigaro on test data, please report them to us at estarikova@rcpcm.org.

## Publication
Elizaveta V. Starikova, Polina O. Tikhonova, Nikita A. Prianichnikov, Chris M. Rands, Evgeny M. Zdobnov, Vadim M. Govorun (2019), Phigaro: high throughput prophage sequence annotation, bioRxiv 598243; doi: https://doi.org/10.1101/598243

(c) E.Starikova, P. Tikhonova, N.Pryanichnikov, 2019
