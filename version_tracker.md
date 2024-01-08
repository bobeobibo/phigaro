## V2.4.0
- Restored a compatibility with Python versions `> 3.7.1`.
- `.pickle` files, containing data neccasary for the work of the tool, were replaced with `.json` and `.csv` files to resolve compatibility issues.
- Added prophage IDs across outputs to improve compatibility between files.
- Fixed a bug with `gff3` and `bed` files formats: prophage coordinates were shifted by 1 nucleotide upstream in versions `phigaro <= 2.3.0`.

## V2.3.0
Added a `--save-fasta` option.

## V2.2.6
Minor corrections. Docker & Singularity containers. What_the_phage implementation.

## V2.2.5
A locate exception was added. So, if the user does not have this tool the configuration of Phigaro will not fail.

## V2.2.4-1
Minor corrections and optional temporary files saving

## V2.2.3
Code style: black. Output parameter corrections.

## V2.2.2
This version is absent.

## V2.2.1
! IMPORTANT !\
Updated thresholds for abs and without_gc modes.

## V2.2.0
New parameter:
 -m, --mode \
Runs the tool at one of the available modes: 
1. basic - find phages using phage score and GC content.
2. abs - find phages using phage score and GC content deviation.
3. without_gc - find phages using phage score only.

## V2.1.10
New output formats: 
  - gff3;
  - bed.
  
New parameter:
  -d, --delete-shorts \
Allows the tool to exclude sequences with length less 20 000 bp automatically.
