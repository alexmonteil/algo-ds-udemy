# takes 2 integers
# returns true if integers have the same frequency of digits
# false otherwise

def digits_frequency(a,b):
    
    astr = str(a)
    bstr = str(b)
    alen = len(astr)
    blen = len(bstr)
    
    if alen != blen:
        return False
    
    counter1, counter2 = {}, {}
    
    for i in range(alen):
        if astr[i] in counter1:
            counter1[astr[i]] += 1
        else:
            counter1[astr[i]] = 1
        
        if bstr[i] in counter2:
            counter2[bstr[i]] += 1
        else:
            counter2[bstr[i]] = 1
    
    for key in counter1:
        if key not in counter2:
            return False
        
        if counter1[key] != counter2[key]:
            return False
        
    return True


testint1, testint2 = 182, 281
testint3, testint4 = 34, 14
testint5, testint6 = 3589578, 5879385
testint7, testint8 = 22, 222

print(f"Should print True: {str(digits_frequency(testint1, testint2))}")
print(f"Should print False: {str(digits_frequency(testint3, testint4))}")
print(f"Should print True: {str(digits_frequency(testint5, testint6))}")
print(f"Should print False: {str(digits_frequency(testint7, testint8))}")