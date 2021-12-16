from math import ceil

with open('day7input') as f:
    nums= [int(x.strip()) for x in f.readline().split(',')]

nums.sort()

#part 1
median = nums[len(nums)//2]
ans = 0
for x in nums:
    ans+=abs(x-median)
print('---Part 1---')
print(ans)

#part 2

arr = [0]*max(nums)
for i in range(len(arr)):
    for val in nums:
        n = abs(val-i)
        arr[i]+=n*(n+1)/2


print('---Part 2---')
print(min(arr))