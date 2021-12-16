input = []
maxX = 0
maxY = 0

with open('day5input') as f:
    for line in f:
        p = line.strip().split(' -> ')
        x1 = int(p[0].split(',')[0])
        y1 = int(p[0].split(',')[1])
        x2 = int(p[1].split(',')[0])
        y2 = int(p[1].split(',')[1])

        if x1==x2 or y1==y2:
            input.append( ((x1, y1), (x2, y2))  )
            maxX = max(maxX, x1, x2)
            maxY = max(maxY, y1, y2)

grid = []
for x in range(maxY+1):
    grid.append( [0]*(maxX+1))


for op in input:
    x1 = op[0][0]
    y1 = op[0][1]
    x2 = op[1][0]
    y2 = op[1][1]
    if x1==x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            grid[i][x1]+=1
    else:
        for i in range( min(x1, x2), max(x1, x2)+1):
            grid[y1][i]+=1
count = 0

for row in grid:
    for elem in row:
        if elem>=2:
            count+=1

print(count)