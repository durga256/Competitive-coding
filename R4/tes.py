# Case A) A number is more than one higher than the ideal; for example, i = 3, A[i] = 5.

# When i is 3, that means we've seen 3 numbers already, yet there are 5 numbers that are less than 5. 
# That then means that there are at least 2 numbers that are less than 5 that we have not yet seen, 
# which in turn means that there are at least 2 global inversions triggered by this one deviation.

# Case B) A number is more than one lower than the ideal; for example, i = 3, A[i] = 1.

# When i is 3, that means we've seen 3 numbers already, yet only 1 number is less than 1. 
# That then means that at least 2 of the numbers we've seen are higher than 1, 
# which in turn means that we've already triggered at least 2 gobal inversions because 
# of this one deviation.

nums = [1,2,0,3]