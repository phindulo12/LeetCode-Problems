#Greedy Approach

s = "applepenapple"
key = ""
finalString = ""
wordDict = ["apple", "pen"]

for i in range(len(s)):
    key += s[i]
    if key in wordDict:
        finalString += " " + key
        key = ""

wordDicts = finalString.strip().split(" ")
print(wordDicts == wordDict)

































































































