d = ['geeksforgeeks', 'geeks', 'geek', 'geezer']

def f():
    min_len = 1000000
    for i in d:
        min_len = min(min_len, len(i))
    
    result = ""
    for i in range(min_len):

        current = d[0][i]

        for j in d:
            if j[i] != current:
                return result
            
        result += current

    return result

print(f())
