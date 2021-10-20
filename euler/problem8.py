#Variables
bigNumber = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
allNumbers = []
biggest = 0

#Conerts number to string
checkNumber = str(bigNumber)

#For every digit in string
for x in checkNumber:
    #Add digit to list
    numX = int(x)
    allNumbers.append(numX)

#For every set of 13 numbers
for y in range(0, len(allNumbers)-12):
    #Assings all variables to set of 13 consecutive numbers
    num1 = allNumbers[y]
    num2 = allNumbers[y+1]
    num3 = allNumbers[y+2]
    num4 = allNumbers[y+3]
    num5 = allNumbers[y+4]
    num6 = allNumbers[y+5]
    num7 = allNumbers[y+6]
    num8 = allNumbers[y+7]
    num9 = allNumbers[y+8]
    num10 = allNumbers[y+9]
    num11 = allNumbers[y+10]
    num12 = allNumbers[y+11]
    num13 = allNumbers[y+12]
    #Gets product of those numbers
    product = num1*num2*num3*num4*num5*num6*num7*num8*num9*num10*num11*num12*num13

    #Assigns result of biggest product to variable
    if product > biggest:
        biggest = product


#Displays answer
print(biggest)