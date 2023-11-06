class Solution:
    def minTime (self, arr, n, m):
        #code here
        start = max(arr); end = sum(arr)
        while start <= end:
            mid = (start+end)//2
            studentsRequire = 1
            curr_sum = 0
            for i in range(n):
                curr_sum+=arr[i]
                if curr_sum>mid:
                    studentsRequire+=1
                    curr_sum=arr[i]
            if studentsRequire <= m:
                result = mid
                end = mid - 1
            else:
                start = mid+1
    
        return result
    
sol = Solution()
arr = [5,10,30,20,15]
k = 3
print(sol.minTime(arr, len(arr), k))