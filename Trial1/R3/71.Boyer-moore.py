haystack = "WELCOMETOSURANACOLLEGE"
needle = "BOLLEGE"
def bad_match_table(needle):
    d = {}; n = len(needle)
    for i in range(len(needle)):
        d[needle[i]] = n - i - 1

    d[needle[-1]] = n
    d['*'] = n
    return d

def find():
    d = bad_match_table(needle)
    i = 0; m = len(needle); tempm = len(needle)
    while i+tempm-1 < len(haystack) and tempm > 0:
        if haystack[i+tempm-1] == needle[tempm-1]:
            print("Here", haystack[i+tempm-1])
            tempm -= 1
        else:
            if haystack[i+m-1] in d.keys():
                i += d[haystack[i+m-1]]
            else:
                i += d['*']
    
    if tempm:
        return -1
    return i

print(find())
