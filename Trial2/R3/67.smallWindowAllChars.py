from collections import Counter
s = 'aabcbcdbca'
def f():
    distinct = len(set(str))
    dic = {}
    ans = len(str)
    i,j = 0,0
    while i<len(str):
        if str[i] in dic:
            dic[str[i]] += 1
        else:
            dic[str[i]] = 1
        if distinct == len(dic):
            while dic[str[j]] > 1:
                dic[str[j]] -= 1
                j += 1
            ans = min(ans,i-j+1)
        i += 1

    return ans

#f()

# https://leetcode.com/problems/minimum-window-substring/

#My solution
s = "ADOBECODEBABNC"; t = "ABBC"
s = "ADOBECODEBANC"; t = "ABC"
#s = "a"; t = "a"
#s = "a"; t = "aa"
s = 'a'; t = 'b'

def check_d(d, d_t):
    for i in d:
        if d[i] < d_t[i]:
            return False
    return True
def f():
    start = end = 0; ans = len(s)+1
    n = len(s)
    distinct_chars = len(set(t))
    d = {}
    d_t = {}; res = []
    for i in t:
        if i in d_t:
            d_t[i] += 1
        else:
            d_t[i] = 1

    for i in d_t:
        if i not in s:
            return ''
    while end < n:
        while end < n and (len(d) < distinct_chars or not check_d(d, d_t)):
            if s[end] in d:
                d[s[end]] += 1
            elif s[end] in t:
                d[s[end]] = 1
            end += 1
            print('loop 1', d)

        while start < end and check_d(d, d_t):
            print(d, s[start])
            if end-start < ans:
                ans = end-start
                res = [start, end-1]
            if s[start] in d:
                d[s[start]] -= 1
            start += 1
    if res:
        print(res)
        print(s[res[0]:res[1]+1])

#f()

#Elegant solution

t = 'oduc'
s = 'icgdwxapjoqrnvsovofwibnztdakxnxyvqp'

def minWindow(s: str, t: str) -> str:
    if len(s) < len(t): return ''
    
    need, match, l, start, windowLen = Counter(t), 0, 0, 0, len(s) + 1
    
    for r, ch in enumerate(s):
        if ch in need:
            need[ch] -= 1
            match += need[ch] == 0

        while match == len(need):
            if windowLen > r - l + 1:
                start, windowLen = l, r - l + 1
            
            removeCh = s[l]
            l += 1 
            if removeCh in need:
                match -= need[removeCh] == 0
                need[removeCh] += 1
    temp = s[start:start + windowLen]
    if windowLen <= len(s) and temp:
        return temp
    return ''

print(minWindow(s,t))