#Valid Palindrome
s = input().lower()
s = "".join(ch for ch in s if ch.isalnum())
i = 0
j = len(s) - 1
while i < j:
    if s[i] != s[j]:
        print(False)
        break
    i += 1
    j -= 1
else:
    print(True)
# TC : O(n)
# SC : O(1)

#3Sum
nums = list(map(int, input().split()))
nums.sort()
res = []
for i in range(0,len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    one = nums[i]
    left = i + 1
    right = len(nums) - 1
    while left < right:
        total = one + nums[left] + nums[right]
        if total == 0:
            res.append([one,nums[left],nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif total < 0:
            left += 1
        else:
            right -= 1
print(res)
# TC : O(n ** 2)
# SC : O(n ** 2)

