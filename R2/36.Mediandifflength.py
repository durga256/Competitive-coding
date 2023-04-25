def findMedian(self, nums) -> float:
        if len(nums) %2 == 0:
            return (nums[len(nums)//2]+nums[len(nums)//2-1])/2
        return nums[len(nums)//2]

def findMedianSortedArrays(self, nums1, nums2) -> float:
    temp = []
    i = 0; j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            temp.append(nums1[i])
            temp.append(nums1[i])
            i += 1; j += 1
        elif nums1[i] < nums2[j]:
            temp.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            temp.append(nums2[j])
            j += 1
    while i < len(nums1):
        temp.append(nums1[i])
        i += 1
    while j < len(nums2):
        temp.append(nums2[j])
        j += 1
    print(temp)
    return self.findMedian(temp)