# Phigaro v2.2.3
[![PyPI version](https://badge.fury.io/py/phigaro.svg)](https://badge.fury.io/py/phigaro)
![Actions Status](https://github.com/bobeobibo/phigaro/workflows/Phigaro%20Tests/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Updates tracker
You can find the information about updates and releases by [link.](https://github.com/bobeobibo/phigaro/blob/master/version_tracker.md)

## Requirements
* **Python**: Python 2.7, Python 3+ versions are supported. 
`pip` utility is also required (`sudo apt-get install python-pip` on Ubuntu).


* **Prodigal**: Download it from 
[https://github.com/hyattpd/Prodigal/wiki/installation](https://github.com/hyattpd/Prodigal/wiki/installation) 
and follow the instructions.

* **HMMER**: Download it from http://hmmer.org/

* **locate**: In order to install Phigaro, you need `locate`. 
It is present in the latest Ubuntu distributions, 
but in case you don't have it, install it with `sudo apt-get install locate` 

## Installation
### Step 1
#### Via pip
```
pip3 install phigaro --user
```
#### Via conda
```
conda env create -f environment.yml
conda activate phigaro_env
```
Where environment.yml can be downloaded form this repository or created manually:
```
name: phigaro_env
dependencies:
  - python=3.7
  - pip
  - bioconda::prodigal
  - bioconda::hmmer
  - pip:
    - phigaro
```
### Step 2
Create a config file with:
```
phigaro-setup
```
It may take some time, since you are downloading the databases.

## Setup Options
### Root
By default, root permissions are required for the installation. But you can disable it by adding a flag to `phigaro-setup`:
```
phigaro-setup --no-updatedb
```
### All Options
Moreover, you may want to change a path of a config installation file or reconfigurate your Phigaro by adding special flags:
```
phigaro-setup --help
usage: phigaro-setup [-h] [-c CONFIG] [-p PVOG] [-f] [--no-updatedb]

Phigaro setup helper

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Path to a config.yml, default is
                        /home/polly/.phigaro/config.yml (default:
                        /home/polly/.phigaro/config.yml)
  -p PVOG, --pvog PVOG  pvogs directory, default is /home/polly/.phigaro/pvog
                        (default: /home/polly/.phigaro/pvog)
  -f, --force           Force configuration and rewrite config.yml if exists
                        (default: False)
  --no-updatedb         Do not run sudo updatedb (default: False)
```
### Manual Setup
Also, you can manually create/change a `config.yml` file and write the `hmmer`, `prodigal` and `pvogs` paths like it is done in an example below. Other parameters should stay the same for the proper work of Phigaro unless you want to change them on purpose.

For the `pvogs` you should download all the files to the `pvog` (or any other folder) via the [link](http://download.ripcm.com/phigaro/) unless it wasn't done previously by `phigaro-setup`.
```
hmmer:
  bin: /usr/bin/hmmsearch
  e_value_threshold: 0.00445
  pvog_path: /home/user/.phigaro/pvog/allpvoghmms
phigaro:
  penalty_black: 2.2
  penalty_white: 0.7
  threshold_max: 46.0
  threshold_min: 45.39
  window_len: 32
prodigal:
  bin: /usr/local/bin/prodigal
```

## Usage

```
phigaro -h      

usage: phigaro [-h] [-V] -f FASTA_FILE [-c CONFIG] [-p] [-e EXTENSION [EXTENSION ...]] [-o OUTPUT] [--not-open] [-t THREADS]  
               [-S SUBSTITUTE_OUTPUT] [-d] [-m MODE]

Phigaro is a scalable command-line tool for predictions phages and prophages from nucleid acid sequences

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -f FASTA_FILE, --fasta-file FASTA_FILE
                        Assembly scaffolds/contigs or full genomes, required
  -c CONFIG, --config CONFIG
                        Path to the config file, not required
  -p, --print-vogs      Print phage vogs for each region
  -e EXTENSION [EXTENSION ...], --extension EXTENSION [EXTENSION ...]
                        Type of the output: html, tsv, gff, bed or stdout. Default is html. You can specify several file      
                        formats with a space as a separator. Example: -e tsv html stdout.
  -o OUTPUT, --output OUTPUT
                        Output filename for html and txt outputs. Required by default, but not required for stdout only       
                        output.
  --not-open            Do not open html file automatically, if html output type is specified.
  -t THREADS, --threads THREADS
                        Num of threads (default is num of CPUs=4)
  -S SUBSTITUTE_OUTPUT, --substitute-output SUBSTITUTE_OUTPUT
                        If you have precomputed prodigal and/or hmmer data you can provide paths to the files in the
                        following format: program:address/to/the/file. In place of program you should write hmmer or
                        prodigal. If you need to provide both files you should pass them separetely as two parametres.        
  -d, --delete-shorts   Exclude sequences with length < 20000 automatically.
  -m MODE, --mode MODE  You can launch Phigaro at one of 3 modes: basic, abs, without_gc. Default is basic. Read more about   
                        modes at https://github.com/bobeobibo/phigaro/
```
Running time depends on the size of your input data and the number of CPUs used.
The running time for a metagenomic assembly file of 150MB is about 20 minutes.

## Output
The output can be annotated prophage genome maps (html) or tabular format (text or stdout).

## Test data
Test data is available in `test_data` folder. 
In order to run Phigaro on test data, enter the following command from your Phigaro folder:

```
phigaro -f test_data/Bacillus_anthracis_str_ames.fna -o test_data/Bacillus_anthracis_str_ames -p --not-open
```
This command generates `Bacillus_anthracis_str_ames.phg.html` files in `test_data` folder.
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
Phigaro is tested on Linux systems. For MacOS, you may need to add the following softlink `ln -s /usr/libexec/locate.updatedb /usr/local/bin/updated` and run `brew install wget`. If you encounter any issues while running Phigaro on test data, please report them to us at estarikova@rcpcm.org.

## Publication
Elizaveta V. Starikova, Polina O. Tikhonova, Nikita A. Prianichnikov, Chris M. Rands, Evgeny M. Zdobnov, Vadim M. Govorun (2019), Phigaro: high throughput prophage sequence annotation, bioRxiv 598243; doi: https://doi.org/10.1101/598243

(c) E.Starikova, P. Tikhonova, N.Pryanichnikov, 2019
