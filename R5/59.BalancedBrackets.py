exp = "[()]{}{[()()]()"

def f():
    stack = []
    for i in range(len(exp)):
        if exp[i] == '(' or exp[i] == '{' or exp[i] == '[':
            stack.append(exp[i])
        elif exp[i] == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return False
        elif exp[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif exp[i] == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                return False
            
    if stack:
        return False
    
    return True

print(f())