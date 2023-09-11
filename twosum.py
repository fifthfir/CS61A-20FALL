def twoSum(nums, target):
    for i in range(len(nums)):
        l = i + 1
        for j in range(l, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []
    
twoSum([2,7,11,15], 9)