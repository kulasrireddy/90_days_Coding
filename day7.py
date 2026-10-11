#Second_largest distinct element in array
nums = list(map(int, input().split()))
largest = float('-inf')
second_largest = float('-inf')
for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
if second_largest == float('-inf'):
    print(-1)
else:
    print(second_largest)


#Move zeros to end
nums = list(map(int, input().split()))
i = 0
for j in range(len(nums)):
    if nums[j] != 0:
        nums[i],nums[j] = nums[j], nums[i]
        i += 1
print(nums)


#Maximum subarray sum
nums = list(map(int, input().split()))
curr_sum = nums[0]
max_sum = nums[0]
for i in range(1,len(nums)):
    curr_sum = max(nums[i],nums[i]+curr_sum)
    max_sum = max(curr_sum,max_sum)
print(max_sum)


#Find Pivot index
nums = list(map(int, input().split()))
left = 0
total = sum(nums)
for i in range(len(nums)):
    right = total - left - nums[i]
    if left == right:
        print(i)
        break
    left += nums[i]
else:
    print(-1)

