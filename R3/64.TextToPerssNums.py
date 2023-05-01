s = "GEEKS FOR GEEKS"

def textToNum():
    nums = ['2','22','222','3','33','333','4','44','444','5','55','555','6','66','666','7','77','777','7777','8','88','888','9','99','999','9999','0']
    res = ""
    for i in range(len(s)):
        if s[i] == " ":
            res += nums[-1]
            continue
        res += nums[ord(s[i])-65]

    print(res)

textToNum()