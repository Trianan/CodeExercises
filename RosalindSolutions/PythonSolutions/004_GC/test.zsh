#!/bin/zsh
SAMPLE_DATASET=./dataset_sample.txt
SAMPLE_OUTPUT='Rosalind_0808
60.919540'
# This wont work and must calculate that the answer falls within a +-0.001 error tolerance.
output="$(python GC.py $SAMPLE_DATASET)"

if [[ "$output" == "$SAMPLE_OUTPUT" ]]; then
    print -P "%F{green}All tests passed.%f\n$output\n"
else
    print -P "%F{red}Test(s) failed.%f\n$output\n"
fi
