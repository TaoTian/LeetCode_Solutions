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
        if len(s) == 1:
            return s in words

        i, j = 0, 1
        while j <= len(s):
            print s[i:j] +' ' +  `i` + ' ' + `j`
            if s[i:j] in words:
                i = j
                j = i + 1
            else:
                j += 1
        return True if i == len(s) else False

Solution().wordBreak('aaaaaaa', ['aaaa', 'aaa'])