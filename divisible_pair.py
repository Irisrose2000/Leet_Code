"""
Problem Statement:
You are given an array of integers and a positive integer 𝑘
find the pairs which is divisible by positive integer k
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def divisibleSumPairs(n, k, arr):
    count = 0
    
    # Loop over all pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            # Check if the sum of the pair is divisible by k
            if (arr[i] + arr[j]) % k == 0:
                count += 1
                
    return count

if __name__ == '__main__':
    # Input handling
    nk = input().split()  # Read input values for n and k
    n = int(nk[0])  # Size of the array
    k = int(nk[1])  # Divisor k
    arr = list(map(int, input().rstrip().split()))  # The array

    # Calling the function and printing the result
    result = divisibleSumPairs(n, k, arr)
    print(result)
