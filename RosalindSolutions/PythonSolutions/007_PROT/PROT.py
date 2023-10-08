import sys
DATASET_FILENAME = sys.argv[1]

with open('rna_codon_table.txt', 'r') as TABLE_FILE:

    # Turn raw table into flat list:
    table_raw = TABLE_FILE.read().split("\n")
    table_raw = [line.split() for line in table_raw]
    tbl = []
    for line in table_raw:
        tbl += line
    table_raw = tbl

    # Turn flat list into compressed dictionary:
    table_clean = {}
    for i in range(1, len(table_raw), 2):
        tbl_key, tbl_val = table_raw[i], table_raw[i-1]
        if tbl_key in table_clean.keys():
            table_clean[tbl_key].append(tbl_val)
        else:
            table_clean[tbl_key] = [tbl_val]
    RNA_CODON_TABLE = table_clean

# Translate RNA string codons into protein string amino-acids:
with open(DATASET_FILENAME, 'r') as rna_str:
    protein_str = ''
    while codon := rna_str.read(3):
        for amino_acid, codons in RNA_CODON_TABLE.items():
            if codon in codons and amino_acid != 'Stop':
                protein_str += amino_acid

print(protein_str)