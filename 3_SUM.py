inputList = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
count = 1
newsum = 0
checkerlist = []

for i in range(len(inputList)):
    newsum = inputList[i]
    for j in range(i + 1, len(inputList)):
        for c in range(j + 1, len(inputList)):
            findC = inputList[c]
            count = count + 1
            newsum = inputList[i] + inputList[j] + findC
            
            if count == 2:
                if newsum == 0:
                    checkerlist.append(inputList[i])
                    checkerlist.append(inputList[j])
                    checkerlist.append(findC)
                    count = 1
                    newsum = inputList[i]
                else:
                    newsum = inputList[i]
                    count = 1

#create a method to add into a 2D array but firstly separate them and sort them
finalList = []
tempList = []
counter = 0

for i in range(len(checkerlist)):
    counter += 1
    tempList.append(checkerlist[i])
    
    if counter == 3:
        tempList.sort()
        if tempList not in finalList:
            finalList.append(tempList)
        tempList = []
        counter = 0

print(finalList)


                
        

    




