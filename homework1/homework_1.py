
import math
from scipy.stats import binom

def calculate_individual_prob_saturated(n):
    # P(E) = 1 - P(E^C) = 1-(1-1/n)^n
    return 1-pow(1-(1/n),n)

def aCb(n, k):
    return math.factorial(n) / (math.factorial(k)*math.factorial(n-k))

def prob_x_bins_empty(N):
    res = 0
    for n in range(1,N):
        if n % 2 == 0:
            res = res - aCb(N, n)*pow((N-n)/N,N)
        else:
            res = res + aCb(N, n)*pow((N-n)/N,N)
        print(1-res,n)

def prob_x_bins_empty(N):
    res = 0
    for n in range(1,N):
        if n % 2 == 0:
            res = res - aCb(N, n)*pow((N-n)/N,N)
        else:
            res = res + aCb(N, n)*pow((N-n)/N,N)
        print(1-res,n)


def k_occupied_input_lines(N):
    p = calculate_individual_prob_saturated(N)
    print(p)
    k = 22
    print(aCb(N,k)*pow(p,k)*pow(1-p,N-k))

    





def main():
    for i in range(1,128+1):
        prob = calculate_individual_prob_saturated(i)
        print("i-> ",i,"Expected aggregated", prob*i, "Expected single", prob)



k_occupied_input_lines(32)