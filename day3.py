# #Missing Number
nums = list(map(int, input().split()))
n = len(nums)
expected_sum = n * (n+1) // 2
actual_sum = 0
for i in range(len(nums)):
    actual_sum += nums[i]
print(expected_sum - actual_sum)

# #count freq of each element in array
nums = list(map(int, input().split()))
freq = {}
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

#Smallest number in array
nums = list(map(int, input().split()))
smallest = float('inf')
for num in nums:
    if num < smallest:
        smallest = num
print(smallest)

#Second smallest distinct element in array
nums = list(map(int, input().split()))
smallest = float('inf')
second_smallest = float('inf')
for num in nums:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num
if second_smallest == float('inf'):
    print(-1)
else:
    print(second_smallest)

#Remove dupliactes from sorted array
nums = list(map(int, input().split()))
i = 0
for j in range(1, len(nums)):
    if nums[j] != nums[i]:
        i += 1
        nums[i] = nums[j]
print(nums[:i+1])

#Maximum diff in array
nums = list(map(int, input().split()))
maxi = float('-inf')
mini = float('inf')
for i in nums:
    if i > maxi:
        maxi = i 
    if i < mini:
        mini = i
print(maxi - mini) 
