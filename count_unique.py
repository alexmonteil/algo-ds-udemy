# write a function which accepts a sorted list and count the unique values.

def count_unique(list):
    
    listlen = len(list)
    if listlen == 0:
        return 0
    elif listlen == 1:
        return 1
    
    left = 0
    right = 1
    
    while right < listlen:
        if list[left] != list[right]:
            left += 1
            list[left] = list[right]
            right += 1
        else:
            right += 1
    
    return left + 1       


# solution 2
def count_unique2(list):
    return len(set(list)) 
        
        

testlist1, testlist2 = [1,1,1,1,1,2], [1,2,3,4,4,4,7,7,12,12,13]
testlist3, testlist4 = [], [-2,-1,-1,0,1]

print(f"Should print 2: {str(count_unique(testlist1))}")
print(f"Should print 7: {str(count_unique(testlist2))}")
print(f"Should print 0: {str(count_unique(testlist3))}")
print(f"Should print 4: {str(count_unique(testlist4))}")  

print(f"Should print 2: {str(count_unique2(testlist1))}")
print(f"Should print 7: {str(count_unique2(testlist2))}")
print(f"Should print 0: {str(count_unique2(testlist3))}")
print(f"Should print 4: {str(count_unique2(testlist4))}") 
   
    
    
    

