# write a function which accepts a list of integers and an integer n
# The function should calculate the maximum sum of n consecutive elements in the list
def max_sublist_sum(list, n):
    listlen = len(list)
    if n >= listlen:
        return sum(list)
    
    start = 0
    end =  n - 1
    subsum = 0
    while end < listlen:
        newsubsum = sum(list[start:end + 1])
        if newsubsum > subsum:
            subsum = newsubsum
        start += 1
        end += 1
        
    return subsum


# better solution
def max_sublist_sum2(list, n):
    maxsum = 0
    tempsum = 0
    listlen = len(list)
    
    if listlen < n:
        return sum(list)
    
    for i in range(n):
        maxsum += list[i]
        
    tempsum = maxsum
    index = n
    while index < listlen:
        tempsum = tempsum - list[index - n] + list[index]
        maxsum = max(maxsum, tempsum)
        index += 1
        
    return maxsum
        


testlist1, testlist2 = [1,2,5,2,8,1,5], [4,2,1,6]

print(f"Should print 10: {str(max_sublist_sum(testlist1, 2))}")
print(f"Should print 17: {str(max_sublist_sum(testlist1, 4))}")
print(f"Should print 6: {str(max_sublist_sum(testlist2, 1))}")


print(f"Should print 10: {str(max_sublist_sum2(testlist1, 2))}")
print(f"Should print 17: {str(max_sublist_sum2(testlist1, 4))}")
print(f"Should print 6: {str(max_sublist_sum2(testlist2, 1))}")