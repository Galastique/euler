#Variables
factors = []
number = 600851475143
prime = 1

#For loop
for prime in range(1, 600851475143):
    #If number is prime, add it to list
    if number % prime == 0:
        factors.append(prime)

        #If all prime factors are found, stop the loop
        result = 1
        for i in factors:
            if result == number:
                print("\n")
                print(factors)
                print("\n")
                print(result)
                exit()
            result *= i