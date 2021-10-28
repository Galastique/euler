#Variables
n = 0
temp = 0

#
for n in range(0, 1000000):

    #if number is even
    if n % 2 == 0:
        n = n/2
        temp+=1

    #if number is odd
    else:
        n = 3*n+1
        temp+=1