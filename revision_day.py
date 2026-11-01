#Largest Number in array
nums = list(map(int, input().split()))
largest = float('-inf')
for num in nums:
    if num > largest:
        largest = num
print(largest)

# #Maximum Subarray(Kadane's Algorithm)
nums = list(map(int, input().split()))
curr_sum = nums[0]
max_sum = nums[0]
for i in range(1, len(nums)):
    curr_sum = max(curr_sum + nums[i],nums[i])
    max_sum = max(curr_sum,max_sum)
print(max_sum)

#Second Largest number
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

#Best Time to Buy and Sell Stock
nums = list(map(int, input().split()))
min_price = nums[0]
max_profit = 0
for num in nums:
    if num < min_price:
        min_price = num
    profit = num - min_price
    if profit > max_profit:
        max_profit = profit
print(max_profit)

#Contains Duplicate
nums = list(map(int, input().split()))
seen = set()
for num in nums:
    if num in seen:
        print(True)
        break
    seen.add(num)
else:
    print(False)

#Product of Array Except Self
nums = list(map(int, input().split()))
ans = [1] * len(nums)
#prefix product (left side sum)
prefix = 1
for i in range(len(nums)):
    ans[i] = prefix
    prefix *= nums[i]

#suffix product(right side sum)
suffix = 1
for i in range(len(nums) - 1, -1,-1):
    ans[i] *= suffix  #Prefix product × Suffix product
    suffix *= nums[i]
print(ans) 