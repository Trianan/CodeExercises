import sys
DATASET_FILENAME = sys.argv[1]

with open(DATASET_FILENAME, "r") as dna_strs:
    dna_a, dna_b = dna_strs.readlines()

hamming_distance = 0
for i in range(len(dna_a)-1):
    if dna_a[i] != dna_b[i]:
        hamming_distance += 1

print(hamming_distance)