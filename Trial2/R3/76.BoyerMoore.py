haystack = 'WELCOMETOSURANACOLLEGE'
needle = 'COLLEGE'

def f():
    bad_match_table = {}
    m = len(needle)

    for i in range(m):
        if needle[i] not in bad_match_table:
            bad_match_table[needle[i]] = m - i - 1

    bad_match_table[needle[m-1]] = m
    bad_match_table['*'] = m

    start = 0; end = m-1; key = end; needle_end = m-1
    while start < end and end < len(haystack):
        print(haystack[start:end+1], end="->")
        if haystack[end] == needle[needle_end]:
            end -= 1
            needle_end -= 1
        else:
            if haystack[key] in bad_match_table:
                start += bad_match_table[haystack[key]]
            else:
                start += bad_match_table['*']
            end = start+m-1
            key = end
            needle_end = m-1
        print(haystack[start:end+1])

    if start == end:
        print(start)
    else:
        print("No match")

f()       