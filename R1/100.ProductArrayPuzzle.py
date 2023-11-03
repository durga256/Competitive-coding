def productExceptSelf(nums, n):
    #code here
    is_zero_present = False; curr_product = 1
    for i in range(len(nums)):
        if nums[i] == 0 and is_zero_present:
            return [0]*len(nums)
        elif nums[i] == 0:
            is_zero_present = True
        else:
            curr_product *= nums[i]
            
    output = []
    for i in range(len(nums)):
        if not is_zero_present or (is_zero_present and nums[i] == 0):
            if nums[i] == 0:
                output.append(int(curr_product))
            else:
                output.append(int(curr_product/nums[i]))
        else:
            output.append(0)
            
    return output