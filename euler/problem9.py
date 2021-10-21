#Variables
a = 0
b = 0
c = 0
answer = 0


#Gets value of a
for a in range(1,400):

    #Gets value of b
    for b in range(a,400):

        #Assigns value to c
        c = 1000-a-b

        #Only runs code if answer hasn't been found
        if answer == 0:

            #This one is pretty self explanatory
            if (a < b) < c:

                #Checks if sum of numbers is equal to 1000
                if a + b + c == 1000:

                    #If number is pythagorean triplet
                    if a*a + b*b == c*c:

                        #Assigns answer
                        answer = a*b*c


#Displays answer
print(answer) #31875000