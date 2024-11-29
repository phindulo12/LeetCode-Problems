nums = [3,2,1,2,1,7]
newnums = []
counter = 0



for c in nums:
    newnums.append(str(c))

for i in range(len(newnums)):
    for j in range(len(newnums)):
        if i == j:
            break
        if newnums[i] == newnums[j]:
            nums[j] = nums[j]+1
            counter += 1
        else:
            continue
print(nums)
