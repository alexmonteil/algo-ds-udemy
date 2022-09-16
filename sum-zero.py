# Write a function that takes a sorted list and returns the first pair that adds to 0

def sum_zero(arr):
    
    left = 0
    right = len(arr) - 1
    
    while left < right:
        sum = arr[left] + arr[right]
        if sum == 0:
            return [arr[left], arr[right]]
        elif sum > 0:
            right -= 1
        else:
            left += 1
            
            

testarr = [-3,-2,-1,0,1,2,3]
testarr2 = [-2,0,1,3]
testarr3 = [1,2,3]
testarr4 = [-3,-1,0,2,4,1,9]

print(f"Should return [-3,3]: {sum_zero(testarr)}")
print(f"Should return None: {sum_zero(testarr2)}")            
print(f"Should return None: {sum_zero(testarr3)}")
print(f"Should return [-1,1]: {sum_zero(testarr4)}")