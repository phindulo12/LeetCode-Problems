import string
class Solution(object):
    def longestIdealString(self, s, k):
        alphabet = string.ascii_lowercase
        calculatinglist = []
        calculatinglist.append(int(alphabet.index(s[0])))
        final_list = []
        final_list.append(s[0])
        difference = 0
        for i in range (1,len(s)) :
            calculatinglist.append(alphabet.index(s[i]))
            if len(calculatinglist) == 2:
                    difference = (calculatinglist[0] - calculatinglist[1])
                    if difference < 0:
                         difference = (difference) * - 1 
                    if difference <= k:
                        final_list.append(s[i])
                        del calculatinglist[:]
                        #calculatinglist.clear()
                        calculatinglist.append(alphabet.index(s[i]))
                    else:
                        del calculatinglist[:]
                        #calculatinglist.clear()
                        # length = len(calculatinglist) - 1 
                        # del calculatinglist[length]
                        calculatinglist.append(alphabet.index(s[i]))
        return (final_list)
    
solution = Solution()
s = "jxhwaysa"
K = 14
print(solution.longestIdealString(s,K))

             
