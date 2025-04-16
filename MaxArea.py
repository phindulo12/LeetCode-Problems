heights = [1,8,6,2,5,4,8,3,7]
maxarea = 0

for i in range(len(heights)):
    for j in range(i+1, len(heights)):
        area = min(heights[i], heights[j]) * (j - i)
        if area > maxarea:
            maxarea = area

print(maxarea)

