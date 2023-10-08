import sys

HD = int(sys.argv[1])
HT = int(sys.argv[2])
HR = int(sys.argv[3])
dominant_allele_P = {
    "HD_HT": 1.0,
    "HD_HR": 1.0,
    "HD_HD": 1.0,
    "HT_HT": 0.75,
    "HT_HR": 0.5,
    "HR_HR": 0.0
}

def get_probability(HD_count, HT_count, HR_count):
    '''
    Calculates probability that two randomly selected mating organisms
    will produce an offspring that possesses a dominant allele.
    '''
    total_count = HD_count + HT_count + HR_count
    selection_denominator = total_count**2 - total_count
    selection_P = {
        # Probabilities for outcomes of selecting 2 random organisms from total.
        "HD_HT": 2 * (HD_count * HT_count) / selection_denominator * dominant_allele_P["HD_HT"],
        "HD_HR": 2 * (HD_count * HR_count) / selection_denominator * dominant_allele_P["HD_HR"],
        "HT_HR": 2 * (HT_count * HR_count) / selection_denominator * dominant_allele_P["HT_HR"],
        "HD_HD": (HD_count**2 - HD_count) / selection_denominator * dominant_allele_P["HD_HD"],
        "HT_HT": (HT_count**2 - HT_count) / selection_denominator * dominant_allele_P["HT_HT"],
        "HR_HR": (HR_count**2 - HR_count) / selection_denominator * dominant_allele_P["HR_HR"]
    }
    P = 0
    for selection_pair, P_dominant_offspring in selection_P.items():
        #print(f"Probability of {selection_pair} producing offspring w. dominant allele: {P_dominant_offspring}")
        P += P_dominant_offspring
    return P

P_ = get_probability(HD, HT, HR)
print(P_)