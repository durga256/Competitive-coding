nums = [100,4,200,1,3,2]

def longestConsecutive():
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = []
        
        for i in range(len(nums)):
            if nums[i] - 1 not in d.keys():
                k = 1
                while nums[i] + k in d.keys():
                    d[nums[i]].append(nums[i] + k)
                    del d[nums[i]+k]; k+= 1
        
        max_length_arr = 0
        for i in d.keys():
            if len(d[i]) >= max_length_arr:
                max_length_arr = len(d[i]) + 1
        print(d)
        return max_length_arr

longestConsecutive()