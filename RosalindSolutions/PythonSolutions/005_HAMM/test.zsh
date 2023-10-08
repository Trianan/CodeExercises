#!/bin/zsh
SAMPLE_DATASET=./dataset_sample.txt
SAMPLE_OUTPUT=7

output="$(python HAMM.py $SAMPLE_DATASET)"

if [[ "$output" == "$SAMPLE_OUTPUT" ]]; then
    print -P "%F{green}All tests passed.%f\n$output\n"
else
    print -P "%F{red}Test(s) failed.%f\n$output\n"
fi
