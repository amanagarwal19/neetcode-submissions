class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m!=n:
            return False

        count = {}
        for i in range(m):
            if count.get(s[i]) is None:
                count[s[i]] = 1
            else:
                count[s[i]] = count[s[i]] + 1

            if count.get(t[i]) is None:
                count[t[i]] = -1
            else:
                count[t[i]] = count[t[i]] - 1

        for _,val in count.items():
            if val != 0:
                # print(count)
                return False
        
        return True