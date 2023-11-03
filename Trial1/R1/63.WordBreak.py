s = "catsandog"; wordDict = ["cats","dog","sand","and","cat"]
#s = "applepenapple"; wordDict = ["apple","pen"]
#s = "leetcode"; wordDict = ["leet","code"]
s = "cars"; wordDict = ["car","ca","rs"]
s = "aaaaaaa"; wordDict = ["aaaa","aaa"]

def wBreak():
    global s
    temp = ""; prev = ""
    wSet = set(wordDict); i = 0
    while i < len(s):
        temp += s[i]
        if temp not in wSet and prev in wSet:
            temp = ""
            s = s[i:]
            i = 0
        else:
            i += 1
        prev = temp
        print(temp)

    if prev in wSet:
        s = s[i:]

    
    if not s:
        return True
    return False

print(wBreak())

