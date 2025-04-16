s = "pwwkew"
Substring = ""
finalsubstring = ""
max_len = 0

for i in s:
    if i not in Substring:
        Substring += i
    else:
        if len(Substring) > max_len:
            max_len = len(Substring)
            finalsubstring = Substring
        Substring = Substring[Substring.index(i)+1:] + i

print(finalsubstring)


