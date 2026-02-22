#recursive
def preorder(root):
    # code here
    res = []
    def helper(root):
        if not root:
            return
        res.append(root.data)
        helper(root.left)
        helper(root.right)
        
    helper(root)
    return res

#Iterative

def preorder(root):
    # code here
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
                res.append(curr.data)
                curr = curr.left
            else:
                curr = pre.right
                pre.right = None
                curr = curr.right
    return res