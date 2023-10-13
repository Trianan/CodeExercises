import sys

P_DOM_PHENO = {
    "HD_HD": 1.0,
    "HD_HT": 1.0,
    "HD_HR": 1.0,
    "HT_HT": 0.75,
    "HT_HR": 0.5,
    "HR_HR": 0.0
}
# Assign argument values to associated keys in PAIR_COUNTS dictionary:
PAIR_COUNTS = {list(P_DOM_PHENO.keys())[i]:int(sys.argv[i+1]) for i in range(6)}
print(PAIR_COUNTS)
