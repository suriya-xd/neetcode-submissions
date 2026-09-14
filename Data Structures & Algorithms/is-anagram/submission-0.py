class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = {}
        map_t = {}
        for i in s:
            if i not in map_s:
                map_s[i] = 0
            else:
                map_s[i] += 1
        for i in t:
            if i not in map_t:
                map_t[i] = 0
            else:
                map_t[i] += 1
        
        if map_s == map_t:
            return True
        else:
            return False