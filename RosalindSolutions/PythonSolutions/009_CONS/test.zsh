#!/bin/zsh
SAMPLE_DATASET=./dataset_sample.txt
SAMPLE_OUTPUT='ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6'

output="$(python CONS.py $SAMPLE_DATASET)"

if [[ "$output" == "$SAMPLE_OUTPUT" ]]; then
    print -P "%F{green}All tests passed.%f\n$output\n"
else
    print -P "%F{red}Test(s) failed.%f\n$output\n"
fi
