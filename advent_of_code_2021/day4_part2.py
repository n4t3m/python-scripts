draws = []
boards = []
current_draws = []
seen = []

def checkBoard(b):
    #check rows
    for r in b:
        row_set = set(r)
        draw_set = set(current_draws)
        if len(row_set.intersection(draw_set))==5:
            return r

    #check columns
    #generate array of column
    for c in range(5):
        col = []
        for i in range(5):
            col.append(b[i][c])    
        col_set = set(col)
        draw_set = set(current_draws)                       
        if len(col_set.intersection(draw_set))==5:
            return col        
    return []

def sumOfUnmarked(b):
    sum = 0
    for r in b:
        for num in r:
            if num not in current_draws:
                sum+=num
    return sum

def partTwo():
    with open('day4input') as f:
        lines = f.readlines()
        draw_input = lines[0].split(',')
        draws = [int(x.strip()) for x in draw_input]
        for i in range(2, len(lines), 6):
            b = []
            for j in range(i, i+5):
                b.append( [int(s.strip()) for s in lines[j].split()]  )
            boards.append(b)
    for draw in draws:
        current_draws.append(draw)
        for b in boards:
            a = checkBoard(b)
            if a!=[]:
                if b not in seen:
                    last = sumOfUnmarked(b)*draw
                    seen.append(b)
    return last

def main():
    print('===Part Two===')
    print(partTwo())
                
main()