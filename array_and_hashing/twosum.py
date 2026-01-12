class Solution(object):
    def twoSum(nums, target):
        for i in range(len(nums)):
            for x in range(i+1, len(nums)):
                if nums[i] + nums[x] == target:
                    y = [i, x]
                    return y
    
    nums = [3, 3]
    target = 6

    result = twoSum(nums=nums, target=target)
    
    print(result)