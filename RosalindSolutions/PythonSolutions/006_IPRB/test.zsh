#!/bin/zsh
SAMPLE_ARGS=(2 2 2)
SAMPLE_OUTPUT=0.78333

output="$(python IPRB.py ${SAMPLE_ARGS[@]})"
# This needs to calculate whether the answer is within tolerance, not an exact match (look up zsh abs()-equivalent)
if [[ "$output" == "$SAMPLE_OUTPUT" ]]; then
    print -P "%F{green}All tests passed.%f\n$output\n"
else
    print -P "%F{red}Test failed: incorrect output.%f\n$output\n"
fi