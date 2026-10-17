#String Rotation
s1 = input()
s2 = input()
if len(s1) != len(s2):
    print(False)
else:
    res = s1 + s1
    if s2 in res:
        print("True")
    else:
        print(False)

#Longest Common Prefix
s = input().split()
res = ""
for word in s:
    if s[word] 

s = input().split()

for i in range(len(s[0])):
    print(s[0][i])

s = input().split()

for i in range(len(s[0])):
    for word in s:
        print(word[i])

#Longest Common Prefix
s = input().split()
res =""
for i in range(len(s[0])):
    for word in s:
        if i >= len(word) or word[i] != s[0][i]:
            print(res)
            exit()
    res += s[0][i]
print(res)
