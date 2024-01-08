# Phigaro v2.4.0
[![PyPI version](https://badge.fury.io/py/phigaro.svg)](https://badge.fury.io/py/phigaro)
![Conda installation](https://anaconda.org/bioconda/phigaro/badges/version.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Phigaro is a standalone command-line application that is able to detect prophage regions taking raw genome and metagenome assemblies as an input. It also produces dynamic annotated “prophage genome maps” and marks possible transposon insertion spots inside prophages. It is applicable for mining prophage regions from large metagenomic datasets.

## Updates tracker
You can find the information about updates and releases by [link.](https://github.com/bobeobibo/phigaro/blob/master/version_tracker.md)

## Documentation: Installation & Usage
Please, follow [the documentation link](https://phigaro.readthedocs.io/) to find installation and usage information.

## Methods overview
Open-reading frames (i.e. proteins) are predicted from the input FASTA file using Prodigal. Phage genes are annotated with prokaryotic viral orthologous groups (pVOGs) profile Hidden Markov Models (HMMs), which can be downloaded stand-alone from http://dmk-brain.ecn.uiowa.edu/pVOGs/. Each contig is represented as a sequence of phage and non-phage genes. A smoothing window algorithm (a triangular window function) determines regions with a high density of phage genes and therefore the prophage regions and boundaries, considering the pVOG annotations and the GC content.

## Known issues
Phigaro is tested on Linux systems. For MacOS, you may need to add the following softlink `ln -s /usr/libexec/locate.updatedb /usr/local/bin/updated` and run `brew install wget`. If you encounter any issues while running Phigaro on test data, please report them to us at estarikova@rcpcm.org.

## Publication
Elizaveta V. Starikova, Polina O. Tikhonova, Nikita A. Prianichnikov, Chris M. Rands, Evgeny M. Zdobnov, Vadim M. Govorun <br>Phigaro: high throughput prophage sequence annotation

- Bioinformatics, 2020; doi: https://doi.org/10.1093/bioinformatics/btaa250
- bioRxiv, 2019; doi: https://doi.org/10.1101/598243

(c) E.Starikova, P. Tikhonova, N.Pryanichnikov, 2019
