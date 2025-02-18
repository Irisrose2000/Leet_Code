## Problem ##
"""
You have N houses, and each house can be painted with one of three colors:
Red
Green
Blue
The cost of painting each house with a specific color is given in three lists:
r[i]: Cost of painting the i-th house Red
g[i]: Cost of painting the i-th house Green
b[i]: Cost of painting the i-th house Blue
Constraints
No two adjacent houses can have the same color.
The goal is to minimize the total cost of painting all house

## SOLUTION ##
"""
class Solution:
    def distinctColoring (self, N, r, g, b):
        for i in range(1,N):
           r[i] += min(g[i-1],b[i-1])# min cost of blue and green
           g[i] += min(r[i-1],b[i-1])# min cost of redand blue
           b[i] += min(r[i-1],g[i-1])#mincost of red and green
           #return the min cost to paint the last house
        return min(g[N-1],b[N-1],r[N-1])
      
        
