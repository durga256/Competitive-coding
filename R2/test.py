haystack = "sadbutsad"; needle = "sad"

def RabinKarp(haystack, needle):
    needle_len = len(needle)
    needle_hash = 0
    for i in range(len(needle)):
        needle_hash += (ord(needle[i])-96)*(2**(needle_len-i-1))

    haystack_hash = 0
    for i in range(needle_len):
        haystack_hash += (ord(haystack[i])-96)*(2**(needle_len-i-1))

    for i in range(len(haystack)-needle_len):
        