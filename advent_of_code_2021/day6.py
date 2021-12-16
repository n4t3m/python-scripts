fishes = []

with open('day6input') as f:
    line = f.readline()
    fishes = [int(x.strip()) for x in line.split(',')]

DAYS = 256

# === FIRST ATTEMPT ===
# build out the list method/too slow for part 2
# start = 0
# while start<DAYS:
#     for i in range(len(fishes)):
#         if fishes[i] == 0:
#             fishes[i]=6
#             fishes.append(8)
#         else:
#             fishes[i]-=1
#     start+=1
# print(len(fishes))

arr = [0]*9
for i in fishes:
    arr[i]+=1

for _ in range(DAYS):
    new_arr = [0]*9
    for i, elem in enumerate(arr):
        if i==0:
            new_arr[6]=elem
            new_arr[8]=elem
        else:
            #values start off as 0
            new_arr[i-1]+=arr[i]
    arr=new_arr

print(sum(arr))