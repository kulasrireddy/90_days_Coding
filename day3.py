#Missing Number
nums = list(map(int, input().split()))
n = len(nums)
expected_sum = n * (n+1) // 2
actual_sum = 0
for i in range(len(nums)):
    actual_sum += nums[i]
print(expected_sum - actual_sum)

#count freq of each element in array
nums = list(map(int, input().split()))
freq = {}
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)