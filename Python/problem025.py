#Variables
fibonacciNumbers = [0, 1]
answer = 0

#Finds fibanacci numbers
while True:

    #Finds next number
    x = fibonacciNumbers[-2] + fibonacciNumbers[-1]
    fibonacciNumbers.append(x)

    #Check length of last number
    if len(str(fibonacciNumbers[-1])) == 1000:

        #Displays answer
        print(len(fibonacciNumbers)-1)  #Expected 4782
        exit()