#!/bin/bash
/root/miniconda3/condabin/conda env list
/root/miniconda3/condabin/conda activate python3
which pip
pip install -r /home/latest_version.txt
phigaro -f /home/test_short_seq.fasta -o output -e html txt gff bed --not-open -d
pip uninstall phigaro 
conda deactivate
echo Phigaro works fine at python3