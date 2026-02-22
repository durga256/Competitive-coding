def toSumTree(self, root) :
    #code here
    def helper(root):
        if not root:
            return 0
        if not root.left and not root.right:
            temp = root.data
            root.data = 0
            return temp
        
        temp = root.data    
        root.data = helper(root.left) + helper(root.right)
        return temp+root.data
        
    helper(root)