# Reverse a string
s = input()
rev = ""
for ch in range(len(s)-1,-1,-1):
    rev += s[ch] 
print(rev)

#Check Palindrome String
s = input()
temp = s
rev = ""
for ch in range(len(s)-1,-1,-1):
    rev += s[ch]
if rev == temp:
    print("Palindrome")
else:
    print("Not Palindrome")


#Palindrome string using two-pointers
s = input()
i = 0
j = len(s) - 1
while i < j:
    if s[i] != s[j]:
        print("Not Palidrome")
        break
    i += 1
    j -= 1
else:
    print("Palindrome")