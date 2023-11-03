#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
arr = [3,5,9,8,7]; x = 23
arr = [0,0,2,1,1]; x = 3
class Solution:
    def fourSum(self, arr, k):
        # code here
        d = {}
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i] + arr[j] not in d:
                    d[arr[i]+arr[j]] = [[i,j]]
                else:
                    d[arr[i]+arr[j]].append([i,j])
        res= []
        for i in d:
            if x-i in d:
                for j in d[i]:
                    for k in d[x-i]:
                        res.append(j+k)
                d[i] = []
                d[x-i] = []

        output = []
        for i in range(len(res)):
            if len(set(res[i])) == len(res[i]):
                output.append(res[i])

        for i in range(len(output)):
            for j in range(len(output[i])):
                output[i][j] = arr[output[i][j]]
            output[i].sort()

        output.sort()

        res = []
        for i in range(len(output)-1):
            for j in range(len(output[i])):
                if output[i][j] != output[i+1][j]:
                    res.append(output[i])
                    break

        if len(output):
            res.append(output[len(output)-1])

        print(res)
        return res


n = Solution()
n.fourSum(arr, x)
        
        
