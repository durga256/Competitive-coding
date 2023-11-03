b = "11010"

def find_bad(arr):
    bad = 0
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] != prev:
            bad += 1
        elif i %2 != 0 and arr[i] == prev:
            bad += 1
    return bad


def stri():
    n = len(b)
    temp = b + b
    #first window
    bad = min_bad = find_bad(temp[:n])
    for i in range(len(temp)-n):
        temp_val = find_bad(temp[i+1:i+n+1])
        min_bad = min(min_bad,temp_val)
        print(temp[i+1:i+n+1], temp_val)
        

        
    
stri()

    


        




    

