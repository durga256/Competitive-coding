s = "()[]{}"

def find():
    stack = []
    for i in s:
        if i == "(" or i == "{" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif i == "}":
            if stack[-1] == "{":
                stack.pop()
            else:
                return False
        elif i == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                return False
            
    if stack:
        return False
    return True
            

print(find())