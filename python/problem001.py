#Variables
answer = 0

#Finds the multiples of 3 or 5 under 1000
for x in range(1,1000):
    if x % 3 == 0 or x % 5 == 0:
        answer+=x

#Displays answer
print(answer) #Expected 233168