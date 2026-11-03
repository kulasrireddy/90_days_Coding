# # Reomve duplicates from sorted array
nums = list(map(int, input().split()))
i = 0
for j in range(1, len(nums)):
    if nums[j] != nums[i]:
        i += 1
        nums[i] = nums[j]
print(nums[:i+1])

#Container with most water
nums = list(map(int, input().split()))
i = 0
j = len(nums) - 1
max_area = 0
while i < j:
    area = min(nums[i],nums[j]) * (j - i)
    max_area = max(area, max_area)
    if nums[i] < nums[j]:
        i += 1
    elif nums[i] > nums[j]:
        j -= 1
    else:
        j -= 1
print(max_area)