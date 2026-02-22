#Recursive

def postOrder(root):
    # code here
    #left->right->root
    res = []
    def helper(root):
        if not root:
            return
        
        helper(root.left)
        helper(root.right)
        res.append(root.data)
        
    helper(root)
    return res

#Iterative using two stacks
def postOrder(root):
    # code here
    #left->right->root
    s1 = []
    s2 = []
    
    s1.append(root)
    
    while s1:
        
        node = s1.pop()
        s2.append(node)
        
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
            
    s2 = [x.data for x in s2]
    
    s2.reverse()
    return s2

#Iterative using one stack
def postOrder(self,node):
    # code here
    res = []
    stack = []
    curr = node
    while True:
        while curr:
            if curr.right:
                stack.append(curr.right)
            stack.append(curr)
            curr = curr.left
            
        curr = stack.pop()
        if curr.right and stack and stack[-1] == curr.right:
            right_child = stack.pop()
            stack.append(curr)
            curr = right_child
        else:
            res.append(curr.data)
            curr = None
            
        if not stack:
            break
            
    return res
