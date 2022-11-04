def isPrime(n):
    if (n == 0 or n == 1):
        return False
    
    for i in range(2,n):
        if (n % i == 0):
            return False
        
    return True

def printPrimes(n):
    for num in range(1,n+1):
        if isPrime(num):
            print(num)
            

printPrimes(100)