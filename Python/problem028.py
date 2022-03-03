#Variables
grid = [[],[],[],[]]
sum = 0

#For every number in 1001^2 grid
for width in range(1, 1001 + 1, 2):
    #Counts numbers in corners
    grid[0].append((width ** 2) - 0 * (width - 1))
    grid[1].append((width ** 2) - 1 * (width - 1))
    grid[2].append((width ** 2) - 2 * (width - 1))
    grid[3].append((width ** 2) - 3 * (width - 1))

    #Adds numbers to sum
    sum += grid[0][-1] + grid[1][-1] + grid[2][-1] + grid[3][-1]

#Displays answer
print(sum - 3) #Expected 669171001