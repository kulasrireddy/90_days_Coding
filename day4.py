#Find the Largest Odd Number

nums = list(map(int, input().split()))
largest = float('-inf')
for num in nums:
    if num > largest:
        largest = num
if largest % 2 != 0:
    print(largest)
else:
    print(-1)


# Find the element that appears only once
nums = list(map(int, input().split()))
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for key, val in freq.items():
    if val == 1:
        print(key)

#single element using XOR
nums = list(map(int, input().split()))
res = 0
for num in nums:
    res ^= num
print(res)

#move all negative numbers to the left side
nums = list(map(int, input().split()))
i = 0
for j in range(0, len(nums)):
    if nums[j] < 0:
        nums[i], nums[j] = nums[j],nums[i]
        i += 1
print(nums)
    