#Two Pointer problems

#Reverse an array(two pointers technique)
nums = list(map(int, input().split()))
i = 0
j = len(nums) - 1
while i < j:
    nums[i],nums[j] = nums[j],nums[i]
    i += 1
    j -= 1
print(nums)
#TC : O(n)
#SC : O(1)

#Check Palindrome Using Two Pointers
s = input()
i = 0
j = len(s) - 1
while i < j:
    if s[i] != s[j]:
        print(False)
        break
    i += 1
    j -= 1
else:
    print(True)
#TC : O(n)
#SC : O(1)


#Pair Sum in a Sorted Array
nums = list(map(int, input().split()))
target = int(input())
i = 0
j = len(nums) - 1
while i < j:
    if nums[i] + nums[j] == target:
        print(True)
        break
    elif nums[i] + nums[j] < target:
        i += 1
    else:
        j -= 1
else:
    print(False)
#TC : O(n)
#SC : O(1)

#Remove Duplicates from a Sorted Array
nums = list(map(int, input().split()))
i = 0
for j in range(1, len(nums)):
    if nums[i] != nums[j]:
        i += 1
        nums[i] = nums[j]
print(nums[:i+1])

nums = list(map(int, input().split()))
i = 0
j = 1
while j < len(nums):
    if nums[i] != nums[j]:
        i += 1
        nums[i] = nums[j]
    j += 1
print(nums[:i+1])

#TC : O(n)
#SC : O(1)

# Move Zeros
nums = list(map(int, input().split()))
i = 0
j = 0
while j < len(nums):
    if nums[j] != 0:
        nums[j],nums[i] = nums[i],nums[j]
        i += 1
    j += 1
print(nums)
for j in range(1, len(nums)):
    if nums[j] != 0:
        nums[j], nums[i] = nums[i],nums[j]
        i += 1
print(nums)
#TC : O(n)
#SC : O(1)

# #Is Subsequence
s = input()
t = input()
i = 0
j = 0
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
    j += 1
if i == len(s):
    print(True)
else:
    print(False)
# # TC : O(n)
# SC : O(1)


# Container With Most Water
nums = list(map(int, input().split()))
i = 0 
j = len(nums) - 1
max_area = 0
while i < j:
    area = min(nums[i] ,nums[j]) * (j - i)
    if nums[i] < nums[j]:
        i += 1
    else:
        j -= 1
    max_area = max(area,max_area)
print(max_area)
# TC : O(n)
# SC : O(1)