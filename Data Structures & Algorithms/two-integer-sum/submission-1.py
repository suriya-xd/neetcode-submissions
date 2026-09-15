class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums)):
            map[nums[i]] = i
        
        for i in range(len(nums)):
            x = target - nums[i]
            if x in map and i!=map[x]:
                return [i, map[x]]
        