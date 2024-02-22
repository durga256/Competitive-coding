def zigZagTraversal(self, root):
    # Your code here
    flag = True
    q = [root]
    res = []
    while q:
        temp = []
        n = len(q)
        for i in range(n):
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            temp.append(node.data)
        flag = not flag
        if flag:
            temp.reverse()
        res += temp
            
    return res