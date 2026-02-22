def integer_to_say(n):
    temp = n[0]; count = 1; res = ""
    for i in range(1,len(n)):
        if temp != n[i]:
            res += str(count)+temp
            temp = n[i]
            count = 1
        else:
            count += 1
    
    res += str(count)+temp 

    return res

def count_say(n):
    temp = "1"
    for i in range(n-1):
        temp = integer_to_say(temp)

    print(temp)

count_say(4)


