#!/bin/zsh
SAMPLE_DATASET='./dataset_sample.txt'
SAMPLE_OUTPUT='20 12 17 21'

output="$(python DNA.py $SAMPLE_DATASET)"

if [[ "$output" == "$SAMPLE_OUTPUT" ]]; then
    print -P "%F{green}All tests passed.%f\n$output\n"
else
    print -P "%F{red}Test failed: incorrect output.%f\n$output\n"
fi