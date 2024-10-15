
# Title: Fermat's Last Theorem Near Misses Finder
# Filename: NearMiss.py
# External Files: None
# External Files Created: None
# Programmers: Ranjith Bhathinolu
# Email: RanjithBhathinolu@lewisu.edu
# Course Number and Section: CPSC-60500-001
# Date: 24th September 2024
# Description: This program helps an interactive user search for near misses of the form (x, y, z, n, k) in the formula 
#              x^n + y^n = z^n, where x, y, z, n, k are positive integers, with 2 < n < 12, and 10 <= x, y <= k.
#              The program finds and displays the smallest relative miss for the given range of values.
# Resources: None


import math

# Function to calculate the relative miss
def calculate_relative_miss(x, y, z, n):
    left_side = x**n + y**n  # Calculate the left side of the equation
    z_n = z**n                # Calculate z raised to the power of n
    z_plus_1_n = (z + 1)**n   # Calculate (z + 1) raised to the power of n
    
    miss = min(abs(left_side - z_n), abs(z_plus_1_n - left_side))  # Find the minimum miss
    relative_miss = miss / left_side  # Calculate relative miss
    
    return relative_miss

# Function to find near misses
def find_near_misses(n, k):
    smallest_relative_miss = float('inf')  # Initialize smallest relative miss
    best_result = None  # Initialize best result
    
    # Iterate through possible values of x and y
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            left_side = x**n + y**n  # Calculate the left side for current x and y
            z = int(math.pow(left_side, 1/n))  # Calculate z as the n-th root of left_side
            
            relative_miss = calculate_relative_miss(x, y, z, n)  # Calculate relative miss
            
            # Update the smallest relative miss and best result if necessary
            if relative_miss < smallest_relative_miss:
                smallest_relative_miss = relative_miss
                best_result = (x, y, relative_miss)
    
    return best_result  # Return the best result found

def main():
    n = int(input("Enter the value of n (2 < n < 12): "))  # Prompt for n
    while n <= 2 or n >= 12:  # Validate n input
        n = int(input("Invalid input. Please enter a value of n between 3 and 11: "))
    
    k = int(input("Enter the value of k (k > 10): "))  # Prompt for k
    while k <= 10:  # Validate k input
        k = int(input("Invalid input. Please enter a value of k greater than 10: "))
    
    x, y, relative_miss = find_near_misses(n, k)  # Find near misses
    
    # Output the results
    print(f"{n}\t{k}\tx= {x}, y= {y}, relative diff= {relative_miss:.6f}")

if __name__ == "__main__":
    main()  # Execute the main function