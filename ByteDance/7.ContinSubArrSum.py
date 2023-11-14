class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_dict = {0: -1}
        remainder = 0
    
        for i in range(len(nums)):
            remainder += nums[i]
            if k != 0:
                remainder %= k
            if remainder in remainder_dict:
                if i - remainder_dict[remainder] >= 2:
                    return True
            else:
                remainder_dict[remainder] = i
        
        return False