nums = [-20, -4, -9, -8, -4, -2, -10, -2]

#naive solution
#O(n^2)

def max_recorded():
    max_recorded_sum = nums[0]
    for i in range(len(nums)):
        max_sum = nums[i]
        current_sum = nums[i]
        for j in range(i+1, len(nums)):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum
        #print(max_sum)
        if max_sum > max_recorded_sum:
            max_recorded_sum = max_sum
    return max_recorded_sum

#print(max_recorded())

# kadane's algo - O(n)

def kadanes():
    max_ending_here = 0
    max_so_far = nums[0]
    for i in range(len(nums)):
        max_ending_here += nums[i]
        print("mazx: ", max_ending_here)
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        # retaining the -ve will only lead to the sum 
        # with the next one being reduced
        # might as well ignore this element and start from next one
        
        # comparison between -ve elements is done before
        # to ensure we capture the smallest -ve incase of all
        # neg elements
        if max_ending_here < 0: 
            max_ending_here = 0
    return max_so_far

print(kadanes())


