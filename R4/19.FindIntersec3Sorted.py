#find common elements In 3 sorted arrays
nums1 = [2,3,4,7]; nums2 = [0,0,3,5]; nums3 = [1,3,8,9]
ar1 = [2,3,4,7]; ar2 = [0,0,3,5]; ar3 = [1,3,8,9]
nums = [nums1,nums2, nums3]

def find_intersection(a,b):
    i = j = 0; res = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            res.append(a[i])
            i += 1; j += 1
        elif a[i] > b[j]:
            j += 1
        elif a[i] < b[j]:
            i += 1
    return res

def intersec():
    res = nums[0]
    for i in range(1,len(nums)):
        res = find_intersection(res, nums[i])
    print(res)

def intersec_3():
    i = j = k = 0; res = []
    while i < len(nums1) and j < len(nums2) and k < len(nums3):
        if nums1[i] == nums2[j] and nums1[i] == nums3[k]:
            res.append(nums1[i])
            i += 1; j += 1; k += 1
        elif nums1[i] > nums2[j] and nums1[i] > nums3[k]:
            j += 1; k += 1
        elif nums2[j] > nums1[i] and nums2[j] > nums3[k]:
            i += 1; k += 1
        elif nums3[k] > nums1[i] and nums3[k] > nums2[j]:
            i += 1; j += 1
    print(res)



intersec_3()

def find_common():
    i = j = k = 0
    res = []
    flag = 0
    while i < len(ar1) and j < len(ar2) and k < len(ar3):
        if ar1[i] == ar2[j] == ar3[k]:
            res.append(ar1[i])
            flag = 1
        current_max = max(ar1[i], ar2[j], ar3[k])
        if ar1[i] < current_max:
            i += 1
        if ar2[j] < current_max:
            j += 1
        if ar3[k] < current_max:
            k += 1
        if flag == 1:
            flag = 0
            i += 1; j += 1; k += 1

        
    res = sorted(list(set(res)))# set to remove repeating intersections and sort to send them in ascending
    return res

print(find_common())

    