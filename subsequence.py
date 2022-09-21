# write a function that takes 2 strings
# the function checks if the first string is a subsequence of the second
# returns True or False

def is_subsequence(str1, str2):
    
    str1len, str2len = len(str1), len(str2)
    i, j = 0, 0
    
    while j < str2len:
        if str1[i] == str2[j]:
            i += 1
            
        if i == str1len:
            return True
        
        j += 1
            
    return False
    
                        


teststr1, teststr2 = "hello", "hello world"
teststr3, teststr4 = "sing", "sting"
teststr5, teststr6 = "abc", "abracadabra"
teststr7, teststr8 = "abc", "acb"

print(f"Should print True: {str(is_subsequence(teststr1, teststr2))}")
print(f"Should print True: {str(is_subsequence(teststr3, teststr4))}")
print(f"Should print True: {str(is_subsequence(teststr5, teststr6))}")
print(f"Should print False: {str(is_subsequence(teststr7, teststr8))}")