#!/bin/zsh
SAMPLE_ARGS=(1 0 0 1 0 1)
SAMPLE_OUTPUT=3.5

output="$(python IEV.py ${SAMPLE_ARGS[@]})"

if [[ "$output" == "$SAMPLE_OUTPUT" ]]; then
    print -P "%F{green}All tests passed.%f\n$output\n"
else
    print -P "%F{red}Test(s) failed.%f\n$output\n"
fi
