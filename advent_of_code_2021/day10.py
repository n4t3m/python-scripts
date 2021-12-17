paths = []

with open('input.txt') as f:
    for line in f.readlines():
        paths.append(line.strip())

p1_point_lookup = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

p2_point_lookup = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

chunk_lookup = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

chunk_reverse_lookup = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

p1_score = 0
p2_scores = []
for path in paths:
    stack = []
    p2str=""
    for c in path:
        if c in chunk_lookup.values():
            stack.append(c)
        else:
            curr = stack.pop()
            if chunk_lookup[c]!=curr:
                p1_score+=p1_point_lookup[c]
                while(len(stack)!=0):
                    stack.pop()
                break
    while len(stack)!=0:
        curr = stack.pop()
        p2str+=chunk_reverse_lookup[curr]
    if p2str!="":
        tmp = 0
        for c in p2str:
            tmp*=5
            tmp+=p2_point_lookup[c]
        p2_scores.append(tmp)
        
p2_scores.sort()

 
print('===Part 1===')
print(p1_score)
print('===Part 2===')
print(p2_scores[len(p2_scores)//2])