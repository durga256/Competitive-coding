#Reverse a string

string = "Hello"

def rev():
    temp = "";
    for i in range(len(string)-1,-1,-1):
        temp += string[i]
    print(temp)

rev()
