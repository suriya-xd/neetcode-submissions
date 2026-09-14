class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = set()
        i = 0
        while i<len(nums):
            if nums[i] not in map:
                map.add(nums[i])
            else:
                return True
            i = i+1
        return False