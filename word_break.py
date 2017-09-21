class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return False
        if not wordDict:
            return False
        words = set(wordDict)
        breakable = [False] * (len(s) + 1)
        breakable[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if breakable[j] and s[j:]

Solution().wordBreak('aaaaaaa', ['aaaa', 'aaa'])
