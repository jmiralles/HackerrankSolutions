# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem

“”””
Task
The final grades for a Physics exam taken by a large group of students have a mean of μ = 70 and a standard deviation of σ = 10. If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:

Scored higher than 80 (i.e., have a > 80 )?
Passed the test (i.e., have a >= 60)?
Failed the test (i.e., have a < 60)?
Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.

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

mean = 70
std = 10

result_1 = 100 * (1 - cumulative(mean, std, 80))
result_2 = 100 * (1 - cumulative(mean, std, 60))
result_3 = 100 * cumulative(mean, std, 60)

print("%.2f" % round(result_1,2))
print("%.2f" % round(result_2,2))
print("%.2f" % round(result_3,2))
