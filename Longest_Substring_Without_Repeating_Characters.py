class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        char_seen, max_len = {}, 0
        st, ed = 0, 0
        while ed < len(s):
            if s[ed] in char_seen:
                max_len = max(max_len, ed - st)
                st, char_seen[s[ed]] = max(char_seen[s[ed]] + 1, st), ed
            else:
                char_seen[s[ed]] = ed
            ed += 1
        return max(max_len, ed - st)

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abbacdef'))
