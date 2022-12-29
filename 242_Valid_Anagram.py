class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        '''

        Solution 1 (better than Solution 2)

        if len(s) != len(t):
            return False
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        for k in s_dict:
            if s_dict[k] != t_dict.get(k, 0):
                return False
        return True

        '''

        # Solution 2
        return sorted(s) == sorted(t)