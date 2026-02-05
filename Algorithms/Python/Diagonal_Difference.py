# Source : https://www.hackerrank.com/challenges/diagonal-difference/
# Author : Rokas Mitka
# Date   : 2/5/2026

# ******************************************************************************************************************************************
#
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#
# For example, the square matrix arr is shown below:
#
# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = 1 + 5 + 9 = 15.
# The right-to-left diagonal = 3 + 5 + 9 = 17.
# Their absolute difference is |15 - 17| = 2.
#
# Function description
#
# Complete the diagonalDifference function with the following parameter:
#
# int arr[n][m] : a 2-D array of integers
# Return
#
# int: the absolute difference in sums along the diagonals
# Input Format
#
# The first line contains a single integer, n, the number of rows and columns in the square matrix arr.
# Each of the next  lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].
#
# Constraints
#
# -100 ≤ arr[i][j] v 100
#
# Sample Input
#
# STDIN      Function
# -----      --------
# 3           arr[][] sizes n = 3, m = 3
# 11 2 4     arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
# 4 5 6
# 10 8 -12
# Sample Output
#
# 15
# Explanation
#
# The primary diagonal is:
#
# 11
#    5
#      -12
# Sum across the primary diagonal: 11 + 5 - 12 = 4.
#
# The secondary diagonal is:
#
#      4
#    5
# 10
# Sum across the secondary diagonal: 4 + 5 + 10 = 19 
# Difference: |4 - 19| = 15
#
# Note: |x| is the absolute value of x.
#
# ******************************************************************************************************************************************

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_diagonal = 0
    right_diagonal = 0
    n = len(arr)
    
    for i in range(len(arr)):
        left_diagonal += arr[i][i]
        
    for j in range(len(arr)):
        right_diagonal += arr[j][n - 1 - j]
        
    difference = abs(left_diagonal - right_diagonal)
    
    return difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
