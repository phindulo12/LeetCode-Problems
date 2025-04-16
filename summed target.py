nums = [2, 4, 3, 5, 7, 8, 9]
target = 10


nums.sort()


count = 0

lists = []


for i in nums:
    j = i + 1
    for j in nums:
        if j + i == 10 :
            if (i,j) and (j,i) not in lists:
                lists.append((i,j))


print(lists)
