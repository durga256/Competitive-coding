s = "this is a test string"
p = "tist"

def f():
    if len(s) < len(p):
        return ""
    dict_p = {}
    for i in range(len(p)):
        if p[i] in dict_p:
            dict_p[p[i]] += 1
        else:
            dict_p[p[i]] = 1

    end = 0; start = 0; temp_dict = {}
    min_len = len(s)+1; count = 0; start_index = -1

    while end < len(s):
        if s[end] in temp_dict:
            temp_dict[s[end]] += 1
        else:
            temp_dict[s[end]] = 1
 
        # If string's char matches with pattern's char then increment count
        if s[end] in dict_p and temp_dict[s[end]] <= dict_p[s[end]]:
            count += 1

        if count == len(p):
            while s[start] not in dict_p or temp_dict[s[start]] > dict_p[s[start]]:
                temp_dict[s[start]] -= 1
                start += 1
            if min_len > end-start+1:
                min_len = end-start+1
                start_index = start
        end += 1 

    print(temp_dict)
    if start_index == -1:
        print("No such window exists")
        return ""

    return s[start_index: start_index + min_len]            
            
print(f())

#Elegant solution

def minWindow(s: str, t: str) -> str:
    if len(s) < len(t): return '-1'
    
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
    return '-1'