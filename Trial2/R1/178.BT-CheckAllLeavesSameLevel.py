def check(self, root):
    #Code here
    s = set()
    def decide(root, level):
        if not root:
            return
        if not root.left and not root.right:
            s.add(level)
            return
            
        decide(root.left, level+1)
        decide(root.right, level+1)
        
    decide(root, 0)
    if len(s) > 1:
        return False
    return True