import sys
DATASET_FILENAME = sys.argv[1]

# Clean dataset
with open(DATASET_FILENAME, 'r') as dna_strs:
    genome, motif = dna_strs.read().split('\n')[:-1]
genome_l, motif_l = len(genome), len(motif)

# Iterate through genome; noting positions of substrings that match motif. 
positions = []
for i in range(0, genome_l - motif_l + 1):
    genome_substr = genome[i : i+motif_l]
    if genome_substr == motif:
        positions.append(str(i+1))
    
print(' '.join(positions))
