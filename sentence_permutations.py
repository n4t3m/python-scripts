from itertools import permutations 

my_list = ["Roses ", "Are ", "Red "]
perms = [''.join(p) for p in permutations(my_list)]
for p in perms:
    print(p)
print("Total Possible Sentences: " + str(len(perms)))
