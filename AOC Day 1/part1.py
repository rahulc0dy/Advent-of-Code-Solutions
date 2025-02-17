file = open("input.txt", "r")

leftList = []
rightList = []
counter = 0

for line in file:
    nums = line.split("   ")
    leftList.append(int(nums[0]))
    rightList.append(int(nums[1]))

leftList.sort()
rightList.sort()

totalDistance = 0

for i in range(len(leftList)):
    totalDistance += abs(leftList[i] - rightList[i])

print(totalDistance)
