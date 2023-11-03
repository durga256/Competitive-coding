s = "abcd"

def f(input, output):
    if len(input) == 0:
        if output:
            print(output, end = " ")
        return
    f(input[1:], output+input[0])
    f(input[1:], output)
    
f(s,"")