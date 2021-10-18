#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.


#Lists for the multiples
multiples = []

#Variables
x = 0

#To find the multiples of 3 or 5 under 1000
while x < 1000:
    if x % 3 == 0 or x % 5 == 0:
        multiples.append(x)
    x += 1
print(multiples)
print("\n")

#Adds each item from the lists
sumTotal = sum(multiples)

#Displays answer
print(sumTotal)