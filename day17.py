# #Find the Duplicate Number
nums = list(map(int, input().split()))
nums.sort()
i = 0
j = 1
while j < len(nums):
    if nums[i] == nums[j]:
        print(nums[i])
    i += 1
    j += 1
# # TC : O(n) and sort is O(n log n)
# # SC : O(1)

#Remove element
nums = list(map(int, input().split()))
val = int(input())
i = 0
j = 0
while j < len(nums):
    if nums[j] != val:
        nums[i] = nums[j]
        i += 1
    j += 1
print(i)
# TC : O(n)
# SC : O(1)