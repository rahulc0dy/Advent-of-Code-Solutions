file = open("input.txt", "r")

leftList = []
rightList = []
counter = 0

for line in file:
    nums = line.split("   ")
    leftList.append(int(nums[0]))
    rightList.append(int(nums[1]))

mp = {}

for item in rightList:
    if mp.get(item):
        mp[item]+=1
    else:
        mp[item]=1

total=0
for item in leftList:
    if mp.get(item):
        total+=item * mp.get(item)

print(total)