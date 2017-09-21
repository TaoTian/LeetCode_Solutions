class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not s:
            return False

        l, r, diff_ct = 0, len(s) - 1, 0
        while l < r:
            if s[l] != s[r] and diff_ct == 0:
                if l + 1 < r and s[l + 1] == s[r] and l < r - 1 and s[l] == s[r - 1]:
                    if l + 2 < r - 1 and s[l + 2] == s[r - 1]:
                        l += 1
                        diff_ct += 1
                    elif l + 1 < r - 2 and s[l + 1] == s[r - 2]:
                        r -= 1
                        diff_ct += 1
                elif l + 1 < r and s[l + 1] == s[r]:
                    l += 1
                    diff_ct += 1
                elif l < r - 1 and s[l] == s[r - 1]:
                    r -= 1
                    diff_ct += 1
                elif l + 1 < r or l < r - 1:
                    return False
            elif s[l] != s[r] and diff_ct:
                return False
            l += 1
            r -= 1
        return True

if __name__ == '__main__':
    print(Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))