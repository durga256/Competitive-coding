from collections import deque

def levelOrder(self,root ):
        # Code here
        q = []
        
        q.append(root)
        res = deque()
        
        while q:
            
            node = q.pop(0)
            res.appendleft(node.data)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
                
        return list(res)