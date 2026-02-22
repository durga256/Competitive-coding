def topView(self,root):
    if not root:
        return []
    node_at_distance = {}
    queue = [(root, 0)]
    res = []
    while queue:
        node, hd = queue.pop(0)
        
        if hd not in node_at_distance:
            node_at_distance[hd] = node.data
            
        if node.left:
            queue.append((node.left, hd-1))
        if node.right:
            queue.append((node.right, hd+1))
            
    for i in sorted(node_at_distance):
        res.append(node_at_distance[i])
        
    return res