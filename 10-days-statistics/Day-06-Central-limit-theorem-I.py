# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem

“”””
Task
A large elevator can transport a maximum of 9800 pounds.
Suppose a load of cargo containing 49 boxes must be transported via the elevator.
The box weight of this type of cargo follows a distribution with a
 mean of μ = 205 pounds and a standard deviation of σ = 15  pounds.
 Based on this information, what is the probability that all 49 boxes
 can be safely loaded into the freight elevator and transported?
“””

import math

def cumulative(mean, std, x):
    parameter = (x - mean) / (std * math.sqrt(2))
    return (0.5) * (1 + erf(parameter))

def erf(z):
    t = 1.0 / (1.0 + 0.5 * math.fabs(z))

    ans = 1 - t * math.exp( -z*z   -   1.26551223 +
                                            t * ( 1.00002368 +
                                            t * ( 0.37409196 +
                                            t * ( 0.09678418 +
                                            t * (-0.18628806 +
                                            t * ( 0.27886807 +
                                            t * (-1.13520398 +
                                            t * ( 1.48851587 +
                                            t * (-0.82215223 +
                                            t * ( 0.17087277))))))))));
    if z >= 0:
        return ans
    else:
        return -ans

mean = 205
std = 15
maxWeight = 9800
n = 49
samplesMean = n * mean;
samplesSTD  = math.sqrt(n) * std

result = cumulative(samplesMean, samplesSTD, maxWeight)

print("%.4f" % result)
