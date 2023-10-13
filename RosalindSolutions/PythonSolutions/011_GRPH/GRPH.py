import sys
DATASET_FILENAME = sys.argv[1]

with open(DATASET_FILENAME, "r") as raw_dataset:
    cleaned_dataset = [(entry.split("\n")[0], "".join(entry.split("\n")[1:])) for entry in raw_dataset.read().split('>')[1:]]

def get_adjacency_list(overlap):
    adjacency_list = []
    for suf_label, suf_str in cleaned_dataset:
        for pre_label, pre_str in cleaned_dataset:
            if suf_str[-overlap:] == pre_str[:overlap] and pre_label != suf_label:
                adjacency_list.append(f"{suf_label} {pre_label}")
    return adjacency_list

print('\n'.join(get_adjacency_list(3)))