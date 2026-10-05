# #largest number in array
# nums = list(map(int, input().split()))
# largest = float('-inf')

# for num in nums:
#     if num > largest:
#         largest = num
# print(largest)        

#second largest distinct number
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