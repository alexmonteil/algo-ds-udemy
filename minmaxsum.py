# write a function that takes an array of 5 integers and returns the max and min sums of any 4 integers in the array

def miniMaxSum(arr):
    
    arrlen = len(arr)
    totalsum = sum(arr, 0)
    minsum = totalsum
    maxsum = 0
    
    for i in range(arrlen):
        currsum = totalsum - arr[i]
        if currsum < minsum:
            minsum = currsum
        
        if currsum > maxsum:
            maxsum = currsum
            
    print(minsum, maxsum)
    
# Testing

arr = [1,2,3,4,5]
miniMaxSum(arr)