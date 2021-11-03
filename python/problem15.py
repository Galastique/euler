#Plugins
import math

#Variables
answer = 0


#Number of possible paths
horizontal = math.factorial(20)
vertical = math.factorial(20)
end = math.factorial(20+20)

#Counts answer (binomial coefficient)
answer = int(end/(horizontal*vertical))

#Displays answer
print(answer)