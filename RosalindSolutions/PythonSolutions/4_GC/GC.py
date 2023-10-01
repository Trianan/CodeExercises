import sys
DATASET_FILENAME = sys.argv[1]

with open(DATASET_FILENAME, "r") as raw_dataset:
    cleaned_dataset = [(entry.split("\n")[0], "".join(entry.split("\n")[1:])) for entry in raw_dataset.read().split('>')[1:]]

gc_contents = []
for entry in cleaned_dataset:
    dna_str = entry[1]
    gc_sum = 0
    for base in dna_str:
        if base == 'G' or base == 'C':
            gc_sum += 1
    gc_content = (gc_sum / len(dna_str)) * 100
    gc_contents.append(gc_content)

max_gc_index = gc_contents.index(max(gc_contents))
print(f"{cleaned_dataset[max_gc_index][0]}\n{gc_contents[max_gc_index]}")
