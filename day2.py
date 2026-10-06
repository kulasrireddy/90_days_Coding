#Reverse of an array

# nums = list(map(int, input().split()))
# i = 0
# j = len(nums) - 1
# while i < j:
#     nums[i],nums[j] = nums[j],nums[i]
#     i += 1
#     j -= 1
# print(nums)

#moves zeros to end
nums = list(map(int, input().split()))
i = 0
for j in range(len(nums)):
    if nums[j] != 0:
        nums[i],nums[j] = nums[j],nums[i]
        i += 1
print(nums)