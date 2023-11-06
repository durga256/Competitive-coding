#https://leetcode.com/problems/maximum-swap/
class Solution:
    def maximumSwap(self, num: int) -> int:
        count_arr = []
        for i in range(10):
            count_arr.append([])
        nums = list(str(num))
        nums = [int(x) for x in nums]

        for i in range(len(nums)):
            count_arr[nums[i]].append(i) 
        
        correct_pos = 0; flag = False
        for i in range(len(count_arr)-1,-1,-1):
            for j in range(len(count_arr[i])):
                if count_arr[i][j] != correct_pos:
                    nums[correct_pos], nums[count_arr[i][-1]] = nums[count_arr[i][-1]], nums[correct_pos]
                    count_arr[i].pop()
                    flag = True
                    break
                elif count_arr[i][j] == correct_pos:
                    correct_pos += 1
            if flag:
                break
        print(count_arr)
        print(nums)

        nums = [str(x) for x in nums]
        return (int(''.join(nums)))