class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        for i in xrange(len(nums)):
            if nums[i] > 0 and nums[i] <= len(nums):
                if nums[i] != i + 1:
                    tmp = nums[i]
                    nums[i] = nums[nums[i] - 1]
                    nums[tmp - 1] = tmp
        for i in xrange(1, len(nums) + 1):
            if nums[i - 1] != i:
                return i
        return i + 1

if __name__ == '__main__':
    print Solution().firstMissingPositive([-10,-3,-100,-1000,-239,1])