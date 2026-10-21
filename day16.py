#Reverse Vowels of a String
s = list(input())
vowels = "aeiouAEIOU"
i = 0
j = len(s) - 1
while i < j:
    if s[i] not in vowels:
        i += 1
    elif s[j] not in vowels:
        j -= 1
    else:
        s[i],s[j] = s[j],s[i]
        i += 1
        j -= 1
print("".join(s)) 
# TC : O(n)
# SC : O(1)