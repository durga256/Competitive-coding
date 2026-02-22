def areMirror(self,root1,root2):
    '''
    :param root1,root2: two root of the given trees.
    :return: True False
    
    '''
    #code here
    def decide(root1, root2):
        if not root1 and not root2:
            return True
        
        if not root2 or not root1:
            return False
            
        if decide(root1.left, root2.right) and decide(root1.right, root2.left):
            if root1.data == root2.data:
                return True
        return False
    
    return decide(root1,root2)