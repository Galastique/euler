#Variables
number = 0

#Squares number
for x in range(1000000000, 1500000000, 10):
    number = x ** 2
    number = str(number)

    #Finds and displays answer
    if (int(number[0]) == 1 and int(number[2]) == 2 and int(number[4]) == 3 and int(number[6]) == 4 and int(number[8]) == 5 and int(number[10]) == 6 and int(number[12]) == 7 and int(number[14]) == 8 and int(number[16]) == 9 and int(number[18]) == 0):
        print(x) #Expected 1389019170
        break