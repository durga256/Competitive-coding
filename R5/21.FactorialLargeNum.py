n = 100
res = [0]*500

def find_factorial():
    res = [0]*500
    res[0] = 1
    res_size = 1

    x = 2
    while x <= n:
        res_size = multiply(x,res, res_size)
        x += 1
        
    for i in range(res_size-1,-1,-1):
        print(res[i], end="")


def multiply(x, res, res_size):
    carry = 0; i = 0

    while i < res_size:
        temp = res[i] * x + carry
        res[i] = temp % 10
        carry = temp // 10
        i += 1

    while (carry):
        res[res_size] = carry % 10
        carry = carry // 10
        res_size += 1

    return res_size

find_factorial()

