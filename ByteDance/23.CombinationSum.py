class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(candidates)
        def solve(idx,sum,lst):
            if idx>=n:
                if sum==target:
                    ans.append(lst)
                return 
            solve(idx+1,sum,lst)
            if sum+candidates[idx]<=target:
                solve(idx,sum+candidates[idx],lst+[candidates[idx]])
        solve(0,0,[])
        return ans