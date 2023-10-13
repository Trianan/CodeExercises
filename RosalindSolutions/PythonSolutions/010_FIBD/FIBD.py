import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

def get_populations(months, mortality):
    newborns = [1, 0]
    adults   = [0, 1]
    seniors  = [0, 0]
    totals   = [1, 1]

    if months < 3:
        return totals
    else:
        for i in range(2, months):
            # Current # newborns are sum of adults and seniors of prev year:
            newborns.append(adults[i-1] + seniors[i-1])

            # Current # adults are prev years newborns, plus newborns up to mortality span.
            adults.append(newborns[i-1])
            for ii in range(2, mortality-1):
                if i - ii >= 0:
                    adults[i] += newborns[i - ii]

            # Current # seniors are # of newborns born mortality-1 years ago.
            if i+1 - mortality >= 0:
                seniors.append(newborns[i+1 - mortality])
            else:
                seniors.append(0)

        # Sum total populations of each month.
        for i in range(2, len(newborns)):
            totals.append(newborns[i] + adults[i] + seniors[i])

    return {
        'newborns': newborns,
        'adults'  : adults,
        'seniors' : seniors,
        'totals'  : totals
    }


pops = get_populations(n, m)
print(pops['totals'][-1])