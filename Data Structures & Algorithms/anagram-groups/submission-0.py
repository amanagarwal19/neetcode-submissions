class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        n = len(strs)
        map = {}
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = ''
            for i in range(26):
                if count[i] != 0:
                    letter = chr(ord('a') + i)
                    cnt = count[i]
                    key = key + letter + str(cnt)
            if key in map:
                map[key].append(s)
            else:
                map[key] = [s]
        
        for k,v in map.items():
            res.append(v)

        return res