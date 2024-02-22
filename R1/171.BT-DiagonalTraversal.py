from collections import defaultdict, deque

def diagonal(self,root):
    #:param root: root of the given tree.
    #return: print out the diagonal traversal,  no need to print new line
    #code here
    d = defaultdict(list)
    
    left_q = deque()
    node = root
    dis = 0
    res = []
    while node:
        d[dis].append(node.data)
        
        if node.left:
            left_q.appendleft((node.left, dis+1))
            
        if node.right:
            node = node.right
        else:
            if left_q:
                node, dis = left_q.pop()
            else:
                break
            
    for i in d:
        res += d[i]
    
    return res