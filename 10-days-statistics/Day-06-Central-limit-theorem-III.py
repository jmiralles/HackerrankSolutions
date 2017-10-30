# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem


“”””
Task

You have a sample of 100 values from a population with mean μ = 500 and with standard deviation σ = 80.
Compute the interval that covers the middle 95% of the distribution of the sample mean; in other words, compute A and B such that P(A<B x <B) = 0.95.
 Use the value of z = 1.96 . Note that z is the z-score.

“””

import math

mean = 500;
std = 80;
n = 100;
zScore = 1.96 #equivalent to 95% confidence interval

# Formula (found online) for confidence interval +/-
marginOfError = zScore * std / math.sqrt(n);

# Print output
print("%.2f" % (mean - marginOfError))
print("%.2f" % (mean + marginOfError))
