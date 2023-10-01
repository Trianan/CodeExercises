import sys

n = int(sys.argv[1])
k = int(sys.argv[2])

def get_population(months, litter_pairs):
    if months < 3:
        return [1 for _ in range(months)]
    else:
        populations = [1, 1]
        for i in range(2, months):
            populations.append(populations[i-2]*litter_pairs + populations[i-1])
        return populations

print(get_population(n, k)[-1])