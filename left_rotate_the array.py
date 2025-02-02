"""
problem
A left rotation operation on an array of size  shifts each of the array's elements  unit to the left.
"""
#solution
import sys

def left_rotate_array(n, d, arr):
    d = d % n  # In case d > n, we only need to rotate d % n times
    rotated_arr = arr[d:] + arr[:d]  # Slice and concatenate
    return rotated_arr

if __name__ == "__main__":
    # Read input
    n, d = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    
    # Perform left rotation
    result = left_rotate_array(n, d, arr)
    
    # Print the result as space-separated values
    print(" ".join(map(str, result)))
