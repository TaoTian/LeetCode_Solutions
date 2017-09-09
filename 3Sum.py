class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        if len(nums) < 3:
            return []

        nums.sort()
        res = []
        for i in xrange(len(nums) - 2):
            if nums[i] == nums[i + 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                while l < r and nums[l] == nums[l + 1]:
                        l += 1
                s = nums[i] + nums[l] + nums[r]
                print i, l, r
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
        return res

if __name__ == '__main__':
    print Solution().threeSum([-1,0,1,2,-1,-4])