class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maps = set(nums)

        res = 0
        for i in nums:
            if i-1 not in maps:
                length = 1
                while (i+length) in maps:
                    length += 1
                res = max(length,res)
            

        return res