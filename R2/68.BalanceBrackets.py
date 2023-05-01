#https://www.geeksforgeeks.org/minimum-number-of-bracket-reversals-needed-to-make-an-expression-balanced/

exp = "}{"
exp = "}{{}}{{{"
exp = "}{}{}{}}}{{{{{}{}{}}{{}{}{}}{{}}{{"

def brack():
    stack = []
    for i in exp:
        if i == "{":
            stack.append(i)
        else:
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)

    print(stack)

    if len(stack) % 2:
        return -1

    ans = 0
    i = 0
    while i < len(stack):
        if stack[i] == stack[i+1]: 
            ans += 1
        else:
            ans += 2
        i += 2

    print(ans)



brack()