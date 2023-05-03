s = "]]][[["

def minSwaps(s):
    count_o = count_c = 0; ans = 0
    for i in range(len(s)):
        if s[i] == "[":
            count_o += 1
        else:
            count_c += 1
        if count_c > count_o:
            ans += 1
            count_c -= 1
            count_o += 1

    print(ans)
    return ans

minSwaps(s)