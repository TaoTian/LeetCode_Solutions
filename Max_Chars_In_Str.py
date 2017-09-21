class Solution(object):
    def max_chars_in_str(self, s):
        if not s:
            return 0

        char_freqs = {}
        most_freq = ['', 0]
        for i in xrange(len(s)):
            if s[i] in char_freqs:
                char_freqs[s[i]] += 1
            else:
                char_freqs[s[i]] = 1

            if char_freqs[s[i]] > most_freq[1]:
                most_freq[0], most_freq[1] = s[i], char_freqs[s[i]]
        return most_freq[0]

if __name__ == '__main__':
    print Solution().max_chars_in_str('accba')