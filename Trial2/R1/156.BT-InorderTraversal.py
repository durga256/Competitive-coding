# Recursive 

def InOrder_help(self,root,res):
    if root:
        self.InOrder_help(root.left,res)
        res.append(root.data)
        self.InOrder_help(root.right,res)
        
    return res
def InOrder(self,root):
    # code here
    res = []
    return self.InOrder_help(root, res)

#Iterative using Morrison Traversal

def InOrder(self,root):
    res = []
    curr = root
    while curr:
        if not curr.left:
            res.append(curr.data)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right
            if not pre.right:
                pre.right = curr
                curr = curr.left
            else:
                curr = pre.right
                res.append(curr.data)
                pre.right = None
                curr = curr.right
                
    return res