
import math
from scipy.stats import binom
import matplotlib.pyplot as plt

def aCb(n, k):
    return math.factorial(n) / (math.factorial(k)*math.factorial(n-k))

def calculate_individual_E_saturated(n):
    # P(E) = 1 - P(E^C) = 1-(1-1/n)^n
    return 1-pow(1-(1/n),n)


def calculate_individual_E_non_saturated(N, prob):
    # Total probability formula
    sum = 0
    for n in range(0,N+1):
        p1 = 1-pow(1-(1/N),n)
        p2 = binom.pmf(n,N,prob)
        sum = sum + (p1*p2)
    #print("N", N, "prob", prob, "sum", sum)
    return sum

def prob_x_bins_empty(N):
    res = 0
    for n in range(1,N):
        if n % 2 == 0:
            res = res - aCb(N, n)*pow((N-n)/N,N)
        else:
            res = res + aCb(N, n)*pow((N-n)/N,N)
        print(res,n)

def calculate_prob_at_least_one_bin_occupied(k, n, m): #N output M input
    res = 0
    for r in range(1, k+1):
        #print(aux)
        if r % 2 == 0:
            res = res - aCb(k, r)* pow(1-r/n, m)
        else:
            res = res + aCb(k, r)* pow(1-r/n, m)
    return res

def plot_non_saturated_2_k(): #N = M
    N = [4,8,32,64]
    prob = 1/2
    for n in N:
        f1 = plt.figure()
        ax1 = f1.add_subplot()
        ax1.set(xlabel='k', ylabel='p(sum(x) = k)', title='N = '+ str(n) +' - Non Saturated switch')
        res = []
        for k in range(0, n+1):
            if k == 0:
                res.append(binom.pmf(k,n,prob)) #Probability input lines are empty
                print(res)
            else:
                res_total_prob = 0;
                for m in range(k, n+1): #total Prob formula for each possible m input
                    aux = 1-calculate_prob_at_least_one_bin_occupied(k, n, m)
                    res_total_prob = res_total_prob + (aux * binom.pmf(m,n,prob)) #num of success m (inputs) in n input lines
                res.append(res_total_prob)
        ax1.plot(list(range(0,n+1)),res)
        #f1.show()
        f1.savefig(str(n)+"_non_saturated_part2.png")

def plot_saturated_2_k():
    N = [4,8,32,64,128]
    for n in N:
        f1 = plt.figure()
        ax1 = f1.add_subplot()
        ax1.set(xlabel='k', ylabel='p(sum(x) = k)', title='N = '+ str(n) +' - Saturated switch')
        res = []
        for k in range(1, n+1):
            res.append(1-calculate_prob_at_least_one_bin_occupied(k, n, n))
        ax1.plot(list(range(1,n+1)),res)
        #f1.show()
        f1.savefig(str(n)+"_saturated_part2.png")

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


#plot_saturated_1()
#plot_non_saturated_1()
#prob_x_bins_empty(32)

#plot_saturated_2_k()
plot_non_saturated_2_k()