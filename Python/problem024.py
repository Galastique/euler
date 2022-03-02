from itertools import permutations

#Finds million's permutation
answer = "".join(list(permutations("0123456789"))[999999])

#Displays answer
print(answer) #Expected 2783915460
