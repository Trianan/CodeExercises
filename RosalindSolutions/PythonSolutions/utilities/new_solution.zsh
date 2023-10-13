#!/bin/zsh

{   
    local current_dir="$(pwd)"
    local solution_dir="$(realpath "$0/../..")/$1"
    mkdir "$solution_dir" && cd "$solution_dir"
    touch ./dataset_{real,sample}.txt
    echo "import sys\nDATASET_FILENAME = sys.argv[1]" > "./${1##[0-9]*_}.py"
    
    echo '#!/bin/zsh
SAMPLE_DATASET=./dataset_sample.txt
SAMPLE_OUTPUT='replace me!'

output="$(python REPLACE_ME.py $SAMPLE_DATASET)"

if [[ "$output" == "$SAMPLE_OUTPUT" ]]; then
    print -P "%F{green}All tests passed.%f\\n$output\\n"
else
    print -P "%F{red}Test(s) failed.%f\\n$output\\n"
fi' > './test.zsh'

    chmod +x ./test.zsh
    cd "$current_dir"
}