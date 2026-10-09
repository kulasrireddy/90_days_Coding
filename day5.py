#Running Sum of 1D Array
nums = list(map(int, input().split()))
res = []
total = 0
for num in nums:
    total += num
    res.append(total)
print(res)

# #Maximum Sum of a Contiguous Subarray
nums = list(map(int, input().split()))
max_sum = float('-inf')
curr_sum = nums[0]
for i in range(1,len(nums)):
    curr_sum = max(nums[i], curr_sum + nums[i])
    max_sum = max(max_sum,curr_sum)
print(max_sum)

#Best Time to Buy and Sell Stock
nums = list(map(int, input().split()))
max_profit = 0
min_price = nums[0]
for i in range(1,len(nums)):
    if nums[i] < min_price:
        min_price = nums[i]
    profit = nums[i] - min_price
    if profit > max_profit:
        max_profit = profit
print(max_profit)

#Find Pivot Index
nums = list(map(int, input().split()))
total = sum(nums)
left = 0
for i in range(len(nums)):
    right = total - nums[i] - left

    if left == right:
        print(i)
        break
    left += nums[i]
else:
    print(-1)