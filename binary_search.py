# function that performs binary search on a list for an element
# returns the index if found or -1 if not found
def binary_search(list, target):
    
    start = 0
    end = len(list) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1


testlist1 = [1,2,3,4,5,6]

print(f"Should print 3: {str(binary_search(testlist1, 4))}")
print(f"Should print 5: {str(binary_search(testlist1, 6))}")
print(f"Should print -1: {str(binary_search(testlist1, 11))}")