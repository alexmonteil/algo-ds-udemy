# write a function that takes 2 lists
# the function should return true if every value in list 1 has its value squared in list 2
# the frequency of values must be the same


def same_squared(list1, list2):
    
    list1len = len(list1)
    list2len = len(list2)
    
    # check for matching lengths
    if list1len != list2len:
        return False
    
    counter1, counter2 = {}, {}
    
    # insert values as keys and their count as values in counters
    for i in range(list1len):
        if list1[i] in counter1:
            counter1[list1[i]] += 1
        else:
            counter1[list1[i]] = 1
            
        if list2[i] in counter2:
            counter2[list2[i]] += 1
        else:
            counter2[list2[i]] = 1
            
    
    # loop to check if counters match
    for key in counter1:
        square = pow(key, 2)
        if  square not in counter2:
            return False
        
        if counter1[key] != counter2[square]:
            return False
    
    return True


testlist1, testlist2 = [1,2,2,3], [1,4,4,9]
testlist3, testlist4 = [1,2,3], [1,4,10]
testlist5, testlist6 = [1,2,6], [1,2,4,5]

print(f"Should print True: {str(same_squared(testlist1, testlist2))}")
print(f"Should print False: {str(same_squared(testlist3, testlist4))}")
print(f"Should print False: {str(same_squared(testlist5, testlist6))}")