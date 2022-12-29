class Solution:

    def twoSum(self, nums, target):
        '''

        Alternate solution

        for ind, i in enumerate(nums):
            if target-i in nums and nums.index(target-i) != ind:
                return [ind, nums.index(target-i)]

        '''
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [i, hashmap[target-nums[i]]]
            hashmap[nums[i]] = i