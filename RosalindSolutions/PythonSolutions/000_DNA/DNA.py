import sys

DATASET_FILENAME = sys.argv[1]

nucleobase_counts = [
    ['A', 0],
    ['C', 0],
    ['G', 0],
    ['T', 0]
]

with open(DATASET_FILENAME, "r") as dna_str:
    for nucleobase in dna_str.read():
        for count in nucleobase_counts:
            if nucleobase == count[0]:
                count[1] += 1

counts = " ".join([str(count[-1]) for count in nucleobase_counts])
print(counts)