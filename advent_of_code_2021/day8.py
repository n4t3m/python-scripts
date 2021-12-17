
with open('day8input') as f:
    part1ans = 0
    part2ans = 0
    for inp in f.readlines():
        nums = [s for s in inp.split('|')[0].strip().split() ]
        msg = [s for s in inp.split('|')[1].strip().split() ]


        key = {}

        # 0 = 6
        # 1 = 2
        # 2 = 5
        # 3 = 5
        # 4 = 4
        # 5 = 5
        # 6 = 6
        # 7 = 3
        # 8 = 7
        # 9 = 6

        #Get Top Segment
        top = ""
        seven = ""
        for n in nums:
            if len(n)==3:
                seven = n
            if len(n)==2:
                one = n
            if len(n)==4:
                four = n
            if len(n)==7:
                eight = n

        for c in seven:
            if c not in one:
                top = c

        #Find 9
        s = set(four + seven)

        for n in nums:
            if len(n)==6:
                dif = 0
                t = set(n)
                for x in t:
                    if x not in s:
                        dif+=1
                if dif==1:
                    nine = n

        botleft = ""
        for c in eight:
            if c not in nine:
                botleft = c



        #Find 5/6
        for n in nums:
            if len(n)==5:
                for m in nums:
                    if len(m)==6:
                        if set(n+botleft) == set(m):
                            five = n
                            six = m

        #find topright
        for n in seven:
            if n not in five:
                topright = n

        #find bot right
        for n in one:
            if n!=topright:
                botright=n

        #find 2, 3, 6
        for n in nums:
            if len(n)==5:
                if topright in n and botright in n:
                    three=n
                elif topright in n and botleft in n:
                    two = n
            if len(n)==6:
                if topright in n and botleft in n:
                    zero = n

        ##populate array with nums
        key[frozenset(zero)] = 0
        key[frozenset(one)] = 1
        key[frozenset(two)] = 2
        key[frozenset(three)] = 3
        key[frozenset(four)] = 4
        key[frozenset(five)] = 5
        key[frozenset(six)] = 6
        key[frozenset(seven)] = 7
        key[frozenset(eight)] = 8
        key[frozenset(nine)] = 9


        outmsg = ""
        for s in msg:
            outmsg+=str(key[frozenset(s)])


        part1lookup = "1478"
        for c in outmsg:
            if c in part1lookup:
                part1ans+=1
        part2ans+=int(outmsg)

print('===Part 1===')
print(part1ans)
print('===Part 2===')
print(part2ans)

