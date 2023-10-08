import sys

DATASET_FILENAME = sys.argv[1]

rna_str = ""
with open(DATASET_FILENAME, "r") as dna_str:
    for nucleobase in dna_str.read():
        if nucleobase == 'T':
            rna_str += 'U'
        else:
            rna_str += nucleobase
print(rna_str)