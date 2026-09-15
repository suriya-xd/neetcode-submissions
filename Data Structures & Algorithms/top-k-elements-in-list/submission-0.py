class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps ={}
        res=[]
        for i in nums:
            maps[i] = 1 + maps.get(i, 0)
        
        sorted_dict = dict(sorted(maps.items(), key=lambda item: item[1], reverse=True))
        sorted_dict = list(sorted_dict.keys())
        for i in range(0,k):
            res.append(sorted_dict[i])
        return res
