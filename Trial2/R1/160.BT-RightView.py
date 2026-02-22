def rightSideView(self, root):
    visit = set()
    if not root:
        return []
    stack = [[root, 0]]
    res = []
    while stack:
        node, level = stack.pop(0)

        if level not in visit:
            visit.add(level)
            res.append(node.val)

        if node.right:
            stack.append([node.right, level+1])
        if node.left:
            stack.append([node.left, level+1])

    return res
def rightSideView(self, root):
    max_level = -1
    res = []
    def helper(root, level):
        nonlocal max_level
        if root:
            if level > max_level:
                res.append(root.val)
                max_level = level
            if root.right:
                helper(root.right, level+1)
            if root.left:
                helper(root.left, level+1)

    helper(root, 0)
    return res