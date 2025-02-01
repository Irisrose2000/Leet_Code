"""
The problem asks you to:

Take a given decimal integer 𝑛
Convert it to its binary representation (base-2).
Then, find the maximum number of consecutive 1s in the binary representation of the number.
"""
#!/bin/python3

import math
import os
import random
import re
import sys
 
def consective_ones(n):
    binary_rep = bin(n)[2:]
    ones_segment=binary_rep.split('0')
    return max(len(segment) for segment in ones_segment)
    



if __name__ == '__main__':
    n = int(input())
    print(consective_ones(n))
