#answer is 104743
"""
primeNumbers = [2,3]
number = 5

while len(primeNumbers) < 10001:
    print(primeNumbers)
    for i in range(2, number+1):
        if number % i == 0:
            primeNumbers.append(number)
            number = number+2
            print(primeNumbers)
"""
primeNumbers = []
def primes():
    
    for i in range(2, 120000):
        fuckOff = 0
        for j in range(2, i):
            if i % j == 0:
                fuckOff = 1
        if fuckOff == 0 or i ==2:
            #print(i)
            primeNumbers.append(i)
            #print(len(primeNumbers))
if len(primeNumbers) < 10001:
    primes()

print(primeNumbers)
print(len(primeNumbers))