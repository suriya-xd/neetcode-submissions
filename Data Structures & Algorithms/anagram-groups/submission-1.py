class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26  # a-z (26 characters)
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Convert list to tuple so it can be hashed as a dictionary key
            res[tuple(count)].append(s) 
            
        return list(res.values())