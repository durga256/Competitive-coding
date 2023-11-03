l = ["cat", "dog", "tac", "god", "act"]

def hash_string(s):
    hash_val = 0
    for i in s:
        hash_val += ord(i)*(2**((ord(i)-96)%13))

    return hash_val

def f():
    d = {    }
    for i in l:
        temp = hash_string(i)
        if temp in d:
            d[temp].append(i)
        else:
            d[temp] = [i]

    for i in d:
        print(d[i])
    

f()

