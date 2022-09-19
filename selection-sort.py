def selection_sort_decreasing(arr):
    i = len(arr) - 2
    while i > 0:
        key = arr[i]
        j = i - 1
        while arr[j] < arr[i]:
            arr[i] = arr[j]
            arr[j] = key
            j -= 1;


# problem 2

def func(x,n):
    x = 0
    for i in range(n):
        x = x + 2 ** i
    return x

# sum of powers of 2 from 2^0 to 2^n
# State --> []
# Loop invariant --> before kth iteration x = 2^k - 1 (from geometric series)
# Initialization: base case: i = 0, x = 0
# Maintenance: Inductive step: 2 - 1  + 2^k = 2^k+1 - 1
# Termination: i = n + 1 --> x = 2^n+1 - 1

# problem 3
def reverse_array(arr):
    left = (len(arr) - 1) / 2
    right = len(arr) / 2
    while left >= 0 and right < len(arr):
        swap(arr[left], arr[right])
        left -= 1
        right += 1

def swap(e1, e2):
    temp = e1
    e1 = e2
    e2 = temp

# State --> [left, right]
# Loop invariant --> subarray arr[left+1 : right - 1] does not exist or has been reversed
# Initialization: base case: subarray does not exist in case of even length and is reversed in case of odd length
# Maintenance: assumption: [left + 1 : right - 1] --> kth iteration
# we look at k+1th iteration as inductive step and check correctness of the invariant
# Termination: left = -1, right = len(arr), assumption: loop invariant
# [a: len(arr) - 1] --> full array A
#
# 
# Problem 5
# Consider the problem of adding 2 n bit binary integers, stores in two n-element arrays A and B.
# The sum of the two integers should be stored in binary form in an (n+1) element array C. 
# State the problem formally and write pseudocode for adding the two integers.
# steps:
# allocate the output array; initialize the carry variable
# each output bit should be (A[i] + B[i] + carry) & 1.
# Carry needs to be updated whenever overflow occurs
# Don't forget to update the extra bit in the output array with carry.
