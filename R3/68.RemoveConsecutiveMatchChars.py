def f(s):
    if not s:
        return s
    #print(s)
    stack = [s[0]]
    i = 1
    prev = s[0]
    while i < len(s):
        if stack and prev == s[i]:
            while i < len(s) and prev == s[i]:
                i += 1
            prev = stack.pop()
        else:
            stack.append(s[i])
            prev = s[i]
            i += 1

    if list(s) == stack:
        return ''.join(stack)
    else:
        return f(''.join(stack))
        
print(f(s))
