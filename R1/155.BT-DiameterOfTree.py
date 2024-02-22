def diameter(self,root):
    def findht(root):
        nonlocal maxi
        if root is None:
            return 0
        lh = findht(root.left)
        rh = findht(root.right)
        maxi = max(maxi, lh + rh+1)
        return 1 + max(lh, rh)
    
    maxi = float("-inf")
    findht(root)
    return maxi