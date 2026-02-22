def dupSub(self, root):
    # code here
    s = set()
    res = 0
    def decide(root):
        nonlocal res
        if not root:
            return 'N'
        if not root.left and not root.right:
            return str(root.data)
            
        temp = decide(root.left) +'#'+str(root.data)+'#'+ decide(root.right)
        if temp in s:
            res = 1
        s.add(temp)
        return temp
    
    decide(root)
    #print(s)
    return res