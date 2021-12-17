grid = []

with open('day9input') as f:
    input = f.readlines()
    for line in input:
        t = []
        for c in line.strip():
            t.append(int(c))
        grid.append(t)

risklevel = 0
rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if r+1!=rows and grid[r][c] >= grid[r+1][c]:
            continue
        if r-1!=-1 and grid[r][c] >= grid[r-1][c]:
            continue
        if c+1!=cols and grid[r][c] >= grid[r][c+1]:
            continue
        if c-1!=-1 and grid[r][c] >= grid[r][c-1]:
            continue
        risklevel+=(grid[r][c]+1)
print('===Part 1===')
print(risklevel)

seen = set()
sizes = []
for r in range(rows):
    for c in range(cols):
        if grid[r][c]!=9 and (r, c) not in seen:
            #bfs time??!?!?
            queue = []
            size = 0
            queue.append((r, c))

            while(len(queue)!=0):
                #print('yahallo')
                curr = queue.pop(0)
                if curr in seen:
                    continue
                seen.add((curr[0], curr[1]))
                size+=1
                if curr[0]+1!=rows and 9 != grid[curr[0]+1][curr[1]]:
                    queue.append((curr[0]+1, curr[1]))
                if curr[0]-1!=-1 and 9 != grid[curr[0]-1][curr[1]]:
                    queue.append((curr[0]-1, curr[1]))
                if curr[1]+1!=cols and 9 != grid[curr[0]][curr[1]+1]:
                    queue.append((curr[0], curr[1]+1))
                if curr[1]-1!=-1 and 9 != grid[curr[0]][curr[1]-1]:
                    queue.append((curr[0], curr[1]-1))
            sizes.append(size)
print('===Part 2===')
sizes.sort()
print(sizes[-1]*sizes[-2]*sizes[-3])  




