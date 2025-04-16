nums = [0, 0, 0]
output = []

for i in range(len(nums)):
    pre = []
    for j in range(len(nums)):
        for k in range(len(nums)):
            if i != j and i != k and j != k:
                if nums[i] + nums[j] + nums[k] == 0:
                    pre = sorted([nums[i], nums[j], nums[k]])
                    if pre not in output:
                        output.append(pre)

print(output)



