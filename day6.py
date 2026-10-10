# Majority Element
nums = list(map(int, input().split()))
freq = {}
n = len(nums)
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for key, val in freq.items():
    if freq[key] > n // 2:
        print(key)

# Longest Consecutive Sequence
nums = list(map(int, input().split()))
count = 1
max_count = 1
nums.sort()
for i in range(1, len(nums)):
    if nums[i] == nums[i-1] + 1:  
        count += 1
    elif nums[i] == nums[i-1]:  #handling duplicate values
        continue
    else:
        count = 1
    
    max_count = max(count, max_count)
print(max_count)
