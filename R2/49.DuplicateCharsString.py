s = "madam"

def dupChar():
    d = {}
    for i in s:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
     
    for i in d.keys():
        if d[i] > 1:
            print(i)

dupChar()