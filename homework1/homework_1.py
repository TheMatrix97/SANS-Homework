
import math
from scipy.stats import binom
import matplotlib.pyplot as plt

def calculate_individual_E_saturated(n):
    # P(E) = 1 - P(E^C) = 1-(1-1/n)^n
    return 1-pow(1-(1/n),n)

def calculate_individual_E_non_saturated(N, prob):
    # Total probability formula
    sum = 0
    for n in range(0,N+1):
        p1 = 1-pow(1-(1/N),n)
        p2 = binom.pmf(n,N,prob)
        sum += sum + (p1*p2)
    #print("N", N, "prob", prob, "sum", sum)
    return sum

    

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

def plot_non_saturated_1():
    f1 = plt.figure()
    f2 = plt.figure()
    ax1 = f1.add_subplot()
    ax1.set(xlabel='N', ylabel='E(x)', title='Non-Saturated switch single expected value')
    ax2 = f2.add_subplot()
    ax2.set(xlabel='N', ylabel='sum(N, E(x))', title='Non-Saturated switch aggregated expected value')
    data = []
    dataAgregatted = []
    iList = []
    for i in range(1,128+1):
        e = calculate_individual_E_non_saturated(i, 1/2)
        data.append(e)
        dataAgregatted.append(e*i)
        iList.append(i)
        print("i-> ",i,"Expected aggregated", e*i, "Expected single", e)
    ax1.plot(iList,data)
    f1.savefig("non-saturated-part1.png")
    ax2.plot(iList, dataAgregatted)
    f2.savefig("non-saturated-part1-aggre.png")
    plt.show()

    
def plot_saturated_1():
    f1 = plt.figure()
    f2 = plt.figure()
    ax1 = f1.add_subplot()
    ax1.set(xlabel='N', ylabel='E(x)', title='Saturated switch single expected value')
    ax2 = f2.add_subplot()
    ax2.set(xlabel='N', ylabel='sum(N, E(x))', title='Saturated switch aggregated expected value')
    data = []
    dataAgregatted = []
    iList = []
    for i in range(1,128+1):
        e = calculate_individual_E_saturated(i)
        data.append(e)
        dataAgregatted.append(e*i)
        iList.append(i)
        print("i-> ",i,"Expected aggregated", e*i, "Expected single", e)
    ax1.plot(iList,data)
    f1.savefig("saturated-part1.png")
    ax2.plot(iList, dataAgregatted)
    f2.savefig("saturated-part1-aggre.png")
    plt.show()






def main():
    for i in range(1,128+1):
        prob = calculate_individual_prob_saturated(i)
        print("i-> ",i,"Expected aggregated", prob*i, "Expected single", prob)


plot_saturated_1()
plot_non_saturated_1()