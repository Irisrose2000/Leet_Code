"""
We are given:

A set of numbers from 1 to 𝑛
A target value 𝑘
Our goal is to find two distinct numbers 
a and 𝑏
b (where 1≤a<b≤n) such that:
The bitwise AND operation between them is the highest possible.
The result is strictly less than 𝑘
"""





#!/bin/python3

import math
import os
import random
import re
import sys

def bitwise_and(n, k):
    max_val = (k - 1)
    
    # Check if max_val is a valid AND result
    if (max_val | k) <= n:
        return max_val
    else:
        return max_val - 1

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        n, k = map(int, input().split())
        print(bitwise_and(n, k))
