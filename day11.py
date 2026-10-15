# #Valid Anagram
class Valid:
    def valid_anagram(self,s1:str,s2:str):
        if len(s1) != len(s2):
            return False
        freq1 = {}
        freq2 = {}
        for ch in s1:
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1
        for ch in s2:
            if ch in freq2:
                freq2[ch] += 1
            else:
                freq2[ch] = 1
        return freq1 == freq2
    
v = Valid()
print(v.valid_anagram("listen","slient"))
print(v.valid_anagram("liste","slient"))


# First Non-Repeating Character
s = input()
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
for key, val in freq.items():
    if val == 1:
        print(key)
        break
else:
    print(-1)