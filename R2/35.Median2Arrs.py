#Median of 2 sorted arrays of equal size

nums1 = [1,12,15,26,38]
nums2 = [2,13,17,30,45]

def med():
    l1 = l2 = 0; h1 = h2 = len(nums1)-1
    while h1-l1>1 and h2-l2>1:
        mid1 = (h1-l1)//2 + l1
        mid2 = (h2-l2)//2 + l2
        print(l1,h1,l2,h2)
        if nums1[mid1] == nums2[mid2]:
            return nums1[mid1]
        if nums1[mid1] > nums2[mid2]:
            h1 = mid1;  l2 = mid2
        else:
            h2 = mid2; l1 = mid1
        print(l1,h1,l2,h2)
    print(nums1[l1], nums1[h1], nums2[l2], nums2[h2])
    ans = (max(nums1[l1], nums2[l2])+min(nums1[h1], nums2[h2]))/2
    print(ans)
    

med()
            


