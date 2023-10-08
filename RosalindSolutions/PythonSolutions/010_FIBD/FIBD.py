import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

def get_population(months, mortality):
    if months < 3:
        return [1 for _ in range(months)]
    else:
        populations = [1, 1]
        for i in range(2, months+1):
            populations.append(populations[i-2] + populations[i-1] - (populations[i-mortality] if i > mortality else 0))
        return populations

print(get_population(n, m)[-1])