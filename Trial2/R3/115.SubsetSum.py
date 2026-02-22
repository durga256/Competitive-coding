import sys

sys.stdin = open('CodeForces\input.txt', 'r')
sys.stdout = open('CodeForces\output.txt', 'w')

def get_input():
    N = int(input())

    arr = [int(x) for x in input().split()]

    K = int(input())

    return (arr,N,K)

class Solution:
    def f(self,arr, n, current_sum):
        if current_sum == 0:
            self.dp[n][current_sum] = 1
            return self.dp[n][current_sum]
        if n == 0:
            self.dp[n][current_sum] = 0
            return self.dp[n][current_sum]
        
        if self.dp[n][current_sum] != -1:
            return self.dp[n][current_sum]
        
        if current_sum >= arr[n-1]:
            self.dp[n][current_sum] = self.f(arr, n-1, current_sum) or self.f(arr, n-1, current_sum-arr[n-1])
        else:
            self.dp[n][current_sum] = self.f(arr, n-1, current_sum)
        return self.dp[n][current_sum]
    def isSubsetSum (self, N, arr, sum):
        self.dp = []
        for i in range(len(arr)+1):
            self.dp.append([-1]*(sum+1))
            
        return self.f(arr, N, sum)
    
sol = Solution()
arr, N, sum= get_input()
print(sol.isSubsetSum(N,arr, sum))
