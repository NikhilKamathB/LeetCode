from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs):
        '''
        Solution 1
        res = defaultdict(list)
        for s in strs:
            ctr = [0] * 26
            for c in s:
                ctr[ord(c)-ord('a')] += 1
            res[tuple(ctr)].append(s)
        return res.values()
        '''
        # Solution 2
        res = defaultdict(list)
        for i in strs:
            res[tuple(sorted(i))].append(i)
        return res.values()

        