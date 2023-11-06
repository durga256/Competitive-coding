#https://leetcode.com/problems/closest-dessert-cost/description/
class Solution:
    def knapsack(self,arr,n,target, main_target):
        if target <= 0 or n == 0:
            return 0

        if arr[n-1] <= target:
            temp1 = arr[n-1]+self.knapsack(arr,n-1,target-arr[n-1], main_target)
            temp2 = self.knapsack(arr,n-1,target, main_target)
            if main_target - temp1 >= 0 and main_target-temp1 < main_target-temp2:
                return temp1
            else:
                return temp2 
        else:
            return self.knapsack(arr,n-1,target, main_target)

    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        search_space = []; temp = []

        for i in range(len(toppingCosts)):
            search_space.append(toppingCosts[i])
            search_space.append(toppingCosts[i])

        for i in range(len(baseCosts)):
            temp.append(self.knapsack(search_space, len(search_space), target-baseCosts[i], target)+baseCosts[i])
        temp.sort()
        print(temp)
        res = temp[0]; min_diff = 100000
        for i in range(len(temp)):
            if target-temp[i] < min_diff and temp[i] <= target:
                res = temp[i]
                min_diff = target-temp[i]


        return res