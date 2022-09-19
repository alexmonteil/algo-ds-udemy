# write a function that takes a sorted list of integers and a target average
# function determines if there is a pair in the list that average to the target average
# returns True or False

def average_pair_check(lis, targ):

    def average_pair(x, y):
        return (x + y) / 2

    lislen = len(lis)

    if lislen == 0:
        return False

    left = 0
    right = lislen - 1

    while left < right:
        avg = average_pair(lis[left], lis[right])
        if avg == targ:
            return True
        elif avg > targ:
            right -= 1
        else:
            left += 1
    
    return False


print(f"Should print True: {str(average_pair_check([1,2,3], 2.5))}")
print(f"Should print True: {str(average_pair_check([1,3,3,5,6,7,10,12,19], 8))}")
print(f"Should print False: {str(average_pair_check([-1,0,3,4,5,6], 4.1))}")
