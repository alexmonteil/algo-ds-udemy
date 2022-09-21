# write a function that takes 2 strings
# the function checks if the first string is a subsequence of the second
# returns True or False

def is_subsequence(str1, str2):
    
    i1, i2 = 0, 0
    j1, j2 = len(str1) - 1, len(str2) - 1
    
    
    while i2 <= j2:
        if str2[i2] == str1[0]:
            break
        else:
            i2 += 1
            
    while i1 <= j1:
        if str1[i1] != str2[i2]:
            return False
        i1 += 1
        i2 += 1
        
    return True


teststr1, teststr2 = "hello", "hello world"
teststr3, teststr4 = "sing", "sting"
teststr5, teststr6 = "abc", "abracadabra"
teststr7, teststr8 = "abc", "acb"

print(f"Should print True: {str(is_subsequence(teststr1, teststr2))}")
print(f"Should print False: {str(is_subsequence(teststr3, teststr4))}")
print(f"Should print False: {str(is_subsequence(teststr5, teststr6))}")
print(f"Should print False: {str(is_subsequence(teststr7, teststr8))}")