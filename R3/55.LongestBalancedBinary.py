s = "001110010"
s = "0100110101"

def n():
    count_0 = 0; count_1 = 0; ans = 0
    for i in range(len(s)):
        if s[i] == "0":
            count_0 += 1
        else:
            count_1 += 1
        if count_0 == count_1:
            ans += 1
            count_0 = 0; count_1 = 0
        elif i == len(s) - 1:
            return -1

    if ans == 0:
        return -1
    return ans

print(n())
