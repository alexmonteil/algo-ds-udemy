# given an array of integers and a number
# write a function which finds the maximum sum of a subarray with length equal to the number


def max_subarray_sum(arr, num):
    arrlen = len(arr)
    if arrlen < num or arrlen == 0:
        return None
    
    tempsum = arr[0]
    for i in range(1, num):
        tempsum += arr[i]
        
    index = num
    maxsum = tempsum
    while index < arrlen:
        tempsum = tempsum - arr[index - num] + arr[index]
        if tempsum > maxsum:
            maxsum = tempsum
        index += 1
        
    return maxsum
    


testarray1, testarray2 = [1,2,5,2,8,1,5], [4,2,1,6]

print(f"Should print 10: {str(max_subarray_sum(testarray1, 2))}")
print(f"Should print 17: {str(max_subarray_sum(testarray1, 4))}")
print(f"Should print 6: {str(max_subarray_sum(testarray2, 1))}")
