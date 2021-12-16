horizontal = 0
depth = 0

with open('day2input') as f:
    for line in f:
        parse = line.split()
        if parse[0]=="forward":
            horizontal+=int(parse[1])
        elif parse[0]=="up":
            depth-=int(parse[1])
        else:
            depth+=int(parse[1])

print('===Part 1===')
print(depth*horizontal)
         
horizontal = 0
depth = 0
aim = 0

with open('day2input') as f:
    for line in f:
        parse = line.split()
        if parse[0]=="forward":
            horizontal+=int(parse[1])
            depth += aim * int(parse[1])
        elif parse[0]=="up":
            aim-=int(parse[1])
        else:
            aim+=int(parse[1])

print('===Part 1===')
print(depth*horizontal)