def integer_to_say(n):
    c = n[0]; count = 1; res = ""
    for i in range(1,len(n)):
        if n[i] != c:
            res += str(count) + c
            count = 1
            c = n[i]
        else:
            count += 1

    res += str(count) + c
    return res

def count_n_say():
    n = "1"; 
    for i in range(6):
        n = integer_to_say(n)
        print(n)

count_n_say()
