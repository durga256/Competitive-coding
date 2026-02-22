#https://leetcode.com/problems/search-in-rotated-sorted-array/description/

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]; key = 3

def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:
            if target < nums[m] and target >= nums[l]:
                r = m - 1
            else:
                l = m + 1
            
        else:
            if target <= nums[r] and target > nums[m]:
                l = m + 1
            else:
                r = m - 1
    return -1

def search(self, nums, target):
    def find_pivot(nums):
        l = 0; h = len(nums)-1
        while l <= h:
            mid = (l+h)//2
            if mid != 0 and nums[mid-1] > nums[mid]:
                return mid
            elif mid != len(nums)-1 and nums[mid] > nums[mid+1]:
                return mid+1
            elif nums[mid] > nums[0]:
                l = mid + 1
            else:
                h = mid - 1
        return -1

    pivot_idx = find_pivot(nums)
    if pivot_idx == -1:
        l = 0; h = len(nums)-1
    elif target < nums[0]:
        l = pivot_idx; h = len(nums)-1
    else:
        l = 0; h = pivot_idx-1
    while l <= h:
        mid = (l+h)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            h = mid - 1
    return -1
    