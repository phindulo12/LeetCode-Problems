class Solution(object):
    def mergeAlternately(self, word1, word2):
        mergedWord = ""
        for i in range(len(word1)):
            mergedWord = mergedWord + word1[i]
            if i < len(word2):
                    mergedWord = mergedWord + word2[i]
            if len(word2) > len(word1):
                if i+1 == len(word1):
                    mergedWord = mergedWord + word2[i+1:len(word2)]
            if i+1 > len(word2):
                    mergedWord = mergedWord + word1[i+1:len(word1)]
                    break                  
        return (mergedWord)
    
solution = Solution()
word1 = "ab"
word2 = "pqrs"

print(solution.mergeAlternately(word1, word2))
                
        





    
