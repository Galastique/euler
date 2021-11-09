#Variables
fibonacciNumbers = [0, 1]
answer = 0


#Loop
while True:

    #Finds value of next number and adds them to the list
    x = fibonacciNumbers[-2] + fibonacciNumbers[-1]
    fibonacciNumbers.append(x)

    #Check length of last number
    if len(str(fibonacciNumbers[-1])) == 1000:

        #Gets anwer
        answer = len(fibonacciNumbers)-1

        #Displays answer
        print(answer)  # Expected 4782
        exit()