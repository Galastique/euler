#Variables
words = []
number = ""
letters = 0

#Counting variables
index = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninty","hundred","thousand"]
tens = 0
hundreds = 0
thousands = 0


#For every word from 1 to 1000
for count in range(1,1001):

    if tens == 10:
        hundreds+=1

    if hundreds == 10:
        thousands+=1

    word = index[thousands] + " " + index[hundreds] + " " + index[tens]

    #Adds word to list
    words.append(word)



    tens+=1
    count+=1





#For every word in list of words
for word in len(words):

    #For ever letter in word
    for letter in word:

        if not letter == " ":
            #Counts letter
            letters+=1


#Displays answer
print(words)
print(count)