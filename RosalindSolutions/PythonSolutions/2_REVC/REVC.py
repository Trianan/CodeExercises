import sys
DATASET_FILENAME = sys.argv[1]

base_complements = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

r_compliment = ""
with open(DATASET_FILENAME, "r") as dna_str:
    for nucleobase in dna_str.read():
        if nucleobase.isalpha():
            r_compliment = base_complements[nucleobase] + r_compliment

print(r_compliment)