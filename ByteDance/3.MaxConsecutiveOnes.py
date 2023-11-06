#https://leetcode.com/problems/max-consecutive-ones-iii/description/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0; end = 0; bad = 0; res = 0
        while end < len(nums) and bad < k:
            if nums[end] == 0:
                bad += 1
            end += 1
        res = max(res,end-start)
        while end < len(nums):
            if nums[end] == 0:
                bad += 1
            while bad > k:
                if nums[start] == 0:
                    bad -= 1
                start += 1
            end += 1
            if bad == k:
                res = max(res,end-start)

        return res
