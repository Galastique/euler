#Variables
width = 20
height = 20

across = 0
x = 0
y = 0
answer = 0


#Executes code until the "end of the grid" has been reached
while across < (width+height):
    across+=1
    
    #For each horizontal movement
    for x in range(1,width+1):
        for y in range(1,height+1-x):
            #if x == width and y == height:
            #print(x, y)
            answer+=1



#Displays answer
print(answer)