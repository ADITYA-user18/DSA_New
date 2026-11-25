s = "abcabcbb"

sets = set()
left=0
maxi = 0


for right in range(0,len(s)):

    while s[right] in sets:
        sets.remove(s[left])
        left+=1

    
    sets.add(s[right])
    maxi = max(maxi,right-left+1)



print(maxi)


