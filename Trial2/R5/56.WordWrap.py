s = "Geeks for Geeks presents word wrap problem" 
M = 15
# s = "aaa bb cc ddddd"
# M = 6
temp = s.split(' ')
temp = [3, 5, 9, 10, 3, 10, 6, 5, 9, 8]
M = 13

def cost(n):
    return n*n

def f(words, n, wordIndex, length, remLength):
    if wordIndex == n-1:
        if words[wordIndex] < remLength:
            return 0
        return cost(remLength)
    
    current_word_length = words[wordIndex]

    if current_word_length < remLength:
        if remLength == length:
            return f(words, n, wordIndex+1, length, remLength-current_word_length)
        else:
            temp_min =  min(
                f(words, n, wordIndex+1, length, remLength-current_word_length-1),
                cost(remLength)+f(words, n, wordIndex, length, length)
            )
            print("temp_min", temp_min)
            return temp_min
    else:
        return cost(remLength)+f(words, n, wordIndex, length, length)
    
print(f(temp, len(temp), 0, M, M))
    