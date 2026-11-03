# #Move zeros to end
# nums = list(map(int, input().split()))
# i = 0
# for j in range(len(nums)):
#     if nums[j] != 0:
#         nums[i], nums[j] = nums[j],nums[i]
#         i += 1
# print(nums)

## 3SUM
nums = list(map(int, input().split()))
nums.sort()
res = []
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    one = nums[i]
    left = i + 1
    right = len(nums) - 1
    while left < right:
        total = one + nums[left]+nums[right]
        if total == 0:
            res.append([one, nums[left],nums[right]])
            left += 1
            right -= 1

            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right+1]:
                right -= 1
        elif total < 0:
            left += 1
        else:
            right -= 1
print(res)
