#!/bin/zsh
SAMPLE_DATASET=./dataset_sample.txt
SAMPLE_OUTPUT='2 4 10'

output="$(python SUBS.py $SAMPLE_DATASET)"

if [[ "$output" == "$SAMPLE_OUTPUT" ]]; then
    print -P "%F{green}All tests passed.%f\n$output\n"
else
    print -P "%F{red}Test(s) failed.%f\n$output\n"
fi
