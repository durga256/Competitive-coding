haystack = "sadbutsad"; needle = "sad"

def f():
    needle_hash = 0
    res = []
    window_size = len(needle)
    for i in range(window_size):
        needle_hash += (ord(needle[i])-96)*(26**(window_size-i-1))
    
    haystack_hash = 0
    for i in range(window_size):
        haystack_hash += (ord(haystack[i])-96)*(26**(window_size-i-1))

    if needle_hash == haystack_hash:
        res.append(0)
    for i in range(len(haystack)-window_size):
        haystack_hash -= (ord(haystack[i])-96)*(26**(window_size-1))
        haystack_hash *= 26
        haystack_hash += (ord(haystack[i+window_size])-96)

        if needle_hash == haystack_hash:
            res.append(i+1)

    print(res)

f()