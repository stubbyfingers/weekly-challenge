def two_sum(nums, target):

    l = 0
    r = len(nums) - 1
    
    while l < r:
        sum = nums[l] + nums[r]
        if sum == target:
            return l, r
        else: 
            r -= 1
        l += 1


print(two_sum([2, 5, 11, 17], 7))















































# def two_sum(nums, target):
#     nums == nums.sort()
#     print(nums)

#     l = 0
#     r = len(nums) - 1
#     result = []

#     while l < r:
#         sum = nums[l] + nums[r]
#         print(sum)
        
#         if target > sum:
#             l += 1
#         if target < sum:
#             r -= 1
#         if target == sum:
#             result.append(l)
#             result.append(r)
#         else:
#             return None
#     return result

# nums = [2, 7, 11, 15]

# print(two_sum(nums, 9))