def levelOrder(self,root ):
        # Code here
        q = []
        
        q.append(root)
        res = []
        
        while q:
            res.append(q[0].data)
            node = q.pop(0)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        return res