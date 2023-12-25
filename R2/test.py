haystack = 'WELCOMETOSURANACOLLEGE'
needle = 'SURANA'

def f():
    len_needle = len(needle)
    bad_match_table = {}
    
    for i in range(len_needle):
        bad_match_table[needle[i]] = len_needle-i-1

    bad_match_table['*'] = len_needle
    bad_match_table[needle[-1]] = len_needle

    print(bad_match_table)
    i = j = start = len_needle-1
    while i < len(haystack):
        if needle[j] == haystack[i]:
            i -= 1; j -= 1
        else:
            if haystack[start] in bad_match_table:
                start += bad_match_table[haystack[start]]
            else:
                start += bad_match_table['*']
            i = start
            j = len_needle-1
        if j == 0:
            print(i)
    
    if j == 0:
        print(i)
        
f()
