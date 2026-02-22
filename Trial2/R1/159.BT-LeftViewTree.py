def LeftView(root):
    
    # code here
    q = []
    if not root:
        return []
    q.append((root, 0))
    res = []
    max_level = -1
    while q:
        node, level = q.pop(0)
        if level > max_level:
            max_level = level
            res.append(node.data)
        
        if node.left:
            q.append((node.left, level+1))
        if node.right:
            q.append((node.right, level+1))
    
    return res