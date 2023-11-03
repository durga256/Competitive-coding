s = "Ravi been saying that he had there"

def find():
    strings = s.split(" ")
    min_idx = len(strings)

    for i in range(len(strings)-1,-1,-1):
        temp = strings.index(strings[i])
        if i != temp:
            min_idx = min(min_idx, temp)
        
    if min_idx == len(strings):
        print("No repeat")
        return
    print(strings[min_idx])

find()