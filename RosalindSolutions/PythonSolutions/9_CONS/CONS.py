import sys
DATASET_FILENAME = sys.argv[1]

with open(DATASET_FILENAME, "r") as raw_dataset:
    cleaned_dataset = ["".join(entry.split("\n")[1:]) for entry in raw_dataset.read().split('>')[1:]]

dna_str_l = len(cleaned_dataset[0])

profile_matrix = {
    'A': [0 for _ in range(dna_str_l)],
    'C': [0 for _ in range(dna_str_l)],
    'G': [0 for _ in range(dna_str_l)],
    'T': [0 for _ in range(dna_str_l)]
}

for i in range(dna_str_l):
    for dna_str in cleaned_dataset:
        base = dna_str[i]
        profile_matrix[base][i] += 1

consensus_str = ''
for i in range(dna_str_l):
    max_base, max_count = '', 0
    for base, counts in profile_matrix.items():
        if counts[i] > max_count:
            max_count = counts[i]
            max_base = base
    consensus_str += max_base


print(consensus_str)
for key, val in profile_matrix.items():
    print(f"{key}: {' '.join(map(str, val))}")