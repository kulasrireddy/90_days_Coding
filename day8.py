# Count vowels in a string
s = input()
count = 0
for ch in s.lower():
    if ch in "aeiou":
        count += 1
print(count)


#Count character frequency
s = input()
freq = {}
for ch in s.lower():
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)