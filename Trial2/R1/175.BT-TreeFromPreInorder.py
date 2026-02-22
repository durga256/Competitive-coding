class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None
def buildtree(self, inorder, preorder, n):
    # code here
    # build tree and return root node
    # inorder - left root right
    # preorder - root left right
    if n == 0: return None
    val = preorder[0]
    root = Node(val)
    
    index = inorder.index(val)
    
    nleft = index
    nright = n - index - 1
    
    root.left = self.buildtree(inorder[:index], preorder[1:1+nleft], nleft)
    root.right = self.buildtree(inorder[index+1:], preorder[1+nleft:], nright)
    
    return root