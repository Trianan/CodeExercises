#!/bin/zsh
SAMPLE_ARGS=(5 3)
SAMPLE_OUTPUT=19

output="$(python FIB.py ${SAMPLE_ARGS[@]})"

if [[ "$output" == "$SAMPLE_OUTPUT" ]]; then
    print -P "%F{green}All tests passed.%f\n$output\n"
else
    print -P "%F{red}Test failed: incorrect output.%f\n$output\n"
fi
