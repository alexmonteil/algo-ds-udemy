# write a function that takes 2 strings
# the function should return true if they are anagrams or false if not


def anagram_check(str1, str2):
    
    str1len = len(str1)
    str2len = len(str2)
    
    # check for matching lengths
    if str1len != str2len:
        return False
    
    counter1, counter2 = {}, {}
    
    # insert values as keys and their count as values in counters
    for i in range(str1len):
        if str1[i] in counter1:
            counter1[str1[i]] += 1
        else:
            counter1[str1[i]] = 1
        
        if str2[i] in counter2:
            counter2[str2[i]] += 1
        else:
            counter2[str2[i]] = 1
            
    # loop to check if counters match
    for key in counter1:
        if key not in counter2:
            return False
        
        if counter1[key] != counter2[key]:
            return False
        
    return True


teststr1, teststr2 = "anagram", "nagaram"
teststr3, teststr4 = "robotchicken", "notrobotchicken"
teststr5, teststr6 = "rock", "kora"

print(f"Should print True: {str(anagram_check(teststr1, teststr2))}")
print(f"Should print False: {str(anagram_check(teststr3, teststr4))}")
print(f"Should print False: {str(anagram_check(teststr5, teststr6))}")