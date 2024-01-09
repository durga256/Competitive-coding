s = "111000"
s = '010'
def f(s):
    zeroes_at_even = zeroes_at_odd = 0
    ones_at_even = ones_at_odd = 0

    window = len(s)
    s = s + s

    for i in range(window):
        if i % 2 == 0:
            if s[i] == '0':
                zeroes_at_even += 1
            else:
                ones_at_even += 1
        else:
            if s[i] == '0':
                zeroes_at_odd += 1
            else:
                ones_at_odd += 1

    min_swaps = len(s)
    start =0; end = window
    while end < len(s):
        #print(zeroes_at_even, ones_at_odd, zeroes_at_odd, ones_at_even, min_swaps)
        temp = min(abs(zeroes_at_even)+abs(ones_at_odd),abs(zeroes_at_odd)+abs(ones_at_even))
        if temp < min_swaps:
            print(zeroes_at_even, ones_at_odd, zeroes_at_odd, ones_at_even, min_swaps)
            min_swaps = temp
        if min_swaps == 0:
            print(0)
            return
        if s[start] == '0':
            zeroes_at_even -= 1
        else:
            ones_at_even -= 1
        zeroes_at_even, zeroes_at_odd = zeroes_at_odd, zeroes_at_even
        ones_at_even, ones_at_odd = ones_at_odd, ones_at_even
        if (window-1) % 2 == 0:
            if s[end] == '0':
                zeroes_at_even += 1
            else:
                ones_at_even += 1
        else:
            if s[end] == '0':
                zeroes_at_odd += 1
            else:
                ones_at_odd += 1
        start += 1; end += 1
    print(min_swaps)

    
f(s)