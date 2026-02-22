def isSumTree(self,root):
    # Code here
    def decide(root):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.data
        left_sum = decide(root.left)
        right_sum = decide(root.right)
        if left_sum != -1 and right_sum != -1:
            if root.data != left_sum + right_sum:
                return -1
            return root.data + left_sum+right_sum
        return -1
        
    temp = decide(root)
    if temp != -1:
        return True
    return False