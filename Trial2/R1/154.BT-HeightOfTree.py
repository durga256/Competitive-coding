def height(self, root):
    # code here
    if not root:
        return 0
        
    return 1 + max(self.height(root.right), self.height(root.left))