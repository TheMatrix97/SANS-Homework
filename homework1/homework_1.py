
from scipy import special

def calculate_individual_prob_saturated(n):
    # P(E) = 1 - P(E^C) = 1-(1-1/n)^n
    return 1-pow(1-(1/n),n)











def main():
    for i in range(1,128+1):
        prob = calculate_individual_prob_saturated(i)
        print("i-> ",i,"Expected aggregated", prob*i, "Expected single", prob)



main()