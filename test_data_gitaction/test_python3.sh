#!/bin/bash
conda env list
conda activate python3
pip install -r /home/latest_version.txt
phigaro -f /home/test_short_seq.fasta -o output -e html txt gff bed --not-open -d
pip uninstall phigaro 
conda deactivate
echo Phigaro works fine at python3