numbers = [-1, 0]
target = -1
output = []

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            output.append(i+1)
            output.append(j+1)

print(output)
