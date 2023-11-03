s = 'geeksforgeeg'
s = 'acaaabbbacdddd'
s = 'abccbccba'

def f():
    stack = [s[0]]
    i = 1
    while i < len(s):
        if stack and stack[-1] == s[i]:
            while i < len(s) and stack[-1] == s[i]:
                i += 1
            stack.pop()
        else:
            stack.append(s[i])
            i += 1

    if list(s) == stack:
        return ''.join(stack)
    else:
        return f(''.join(st))

f()
                