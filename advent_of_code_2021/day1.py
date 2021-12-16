## Task 1

nums = []

with open('day1input') as f:
    for line in f:
        nums.append(int(line))

greater_than_prev = 0

for i in range(1, len(nums)):
    if nums[i]>nums[i-1]:
        greater_than_prev+=1

print('===Part 1===')
print(greater_than_prev)

## Task 2

greater_than_prev = 0

for i in range(2, len(nums)-1):
    if nums[i]+nums[i-1]+nums[i+1]>nums[i-1]+nums[i]+nums[i-2]:
        greater_than_prev+=1

print('===Part 2===')
print(greater_than_prev)
