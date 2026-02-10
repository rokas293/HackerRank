# Source : https://www.hackerrank.com/challenges//time-conversion/
# Author : Rokas Mitka
# Date   : 2/10/2026

# ***********************************************************************************************************************************
#
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
#
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
#
# Example
#
# s = '12:01:00PM'
# Return '12:01:00'.
#
# s = '12:01:00AM'
# Return '00:01:00'.
#
# Function Description
#
# Complete the timeConversion function with the following parameter(s):
# string s: a time in 12 hour format
#
# Returns
# string: the time in 12 hour format
#
# Input Format
#
# A single string  that represents a time in 12-hour clock format (i.e.:hh:mm:ssAM or hh:mm:ssPM).
#
# Constraints
#
# All input times are valid
# Sample Input 0
#
# 07:05:45PM
# Sample Output 0
#
# 19:05:45
#
# ***********************************************************************************************************************************


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    hour_str = s[0:2] 
    suffix = s[-2:] # AM/PM
    time_without_suffix = s[2:-2] # Everything except AM/PM and HH
    
    hour = int(hour_str)
    
    if hour == 12 and suffix == "AM":
        hour = 0
    elif 1 <= hour <= 11 and suffix == "PM":
        hour += 12
    elif hour == 12 and suffix == "PM":
        hour = 12
    
    new_hour_str = str(hour).zfill(2)
    
    result = new_hour_str + time_without_suffix
    
    return result
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
