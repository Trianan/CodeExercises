#!/bin/zsh
SAMPLE_ARGS=(6 3)
SAMPLE_OUTPUT=4

output="$(python FIBD.py ${SAMPLE_ARGS[@]})"

if [[ "$output" == "$SAMPLE_OUTPUT" ]]; then
    print -P "%F{green}All tests passed.%f\n$output\n"
else
    print -P "%F{red}Test failed: incorrect output.%f\n$output\n"
fi
