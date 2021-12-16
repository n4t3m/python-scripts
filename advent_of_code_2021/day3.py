input = []

with open('day3input') as f:
    for line in f:
        input.append(line.strip())

gamma = ""
epsilon = ""

#most common goes in gamma

zero_count = [0]*len(input[0])

for s in input:
    for i, x in enumerate(s):
        if x=="0":
            zero_count[i]+=1

for i in range(len(zero_count)):
    if zero_count[i]>len(input)/2:
        gamma+="1"
        epsilon+="0"
    else:
        gamma+="0"
        epsilon+="1"

print('===Part 1===')
print(int(gamma, 2)*int(epsilon, 2))

#Part 2 Start!

iteration = 0
oxygen_vals = input
while len(oxygen_vals)!=1:
    one_count = 0
    #find most common bit
    for val in oxygen_vals:
        if val[iteration]=="1":
            one_count+=1
    if one_count>= len(oxygen_vals) /2:
        #keep numbers where val[iteration]=1
        oxygen_vals = list(filter(lambda x: x[iteration] == "1", oxygen_vals))
    else:
        oxygen_vals = list(filter(lambda x: x[iteration] == "0", oxygen_vals))
    iteration+=1
oxygen_val = oxygen_vals[0]

iteration = 0
co_vals = input
while len(co_vals)!=1:
    one_count = 0
    #find most common bit
    for val in co_vals:
        if val[iteration]=="1":
            one_count+=1
    if one_count < len(co_vals) /2:
        #keep numbers where val[iteration]=1
        co_vals = list(filter(lambda x: x[iteration] == "1", co_vals))
    else:
        co_vals = list(filter(lambda x: x[iteration] == "0", co_vals))
    iteration+=1

co_val = co_vals[0]

print('===Part 2===')
print( int(oxygen_val, 2)*int(co_val, 2) )