s = "aabb"
s = "abc"
# the given string has to be palindrome for this to work
# the swaps should only allows adjacent swaps but this can be tweaked
def swap():
    ls = list(s); res = 0
    while ls:
        i = ls.index(ls[-1])

        if i == len(ls) - 1:
            res += len(ls)//2
        else:
            res += i
            ls.pop(i)
        ls.pop()
    print(res)

swap()