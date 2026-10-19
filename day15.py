#Squares of a Sorted Array
nums = list(map(int, input().split()))
res = [0] * len(nums)
left = 0
right = len(nums) - 1
pos = len(nums) - 1

while left <= right:
    if nums[left] ** 2 > nums[right] ** 2:
        res[pos] = nums[left] ** 2
        left += 1
    else:
        res[pos] = nums[right] ** 2
        right -= 1
    pos -= 1
print(res)
# TC : O(n)
# SC : O(n)

# Sort 0's , 1's , 2's in asc order
#Sort Colors — Dutch National Flag Algorithm
nums = list(map(int, input().split()))
left = 0
mid = 0
right = len(nums) - 1
while mid <= right:
    if nums[mid] == 0:
        nums[mid], nums[left] = nums[left],nums[mid]
        mid += 1
        left += 1
    elif nums[mid] == 1:
        mid += 1
    else:
        nums[mid],nums[right] = nums[right],nums[mid]
        right -= 1
print(nums)
# TC : O(n)
# SC : O(1)