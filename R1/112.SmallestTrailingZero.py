def no_of_fives(n):
    count = 0
    while n/5 >= 1 and n%5 == 0:
        n /= 5
        count += 1

    return count

def findFactorial(n):
    count_of_fives = 1; current_num = 5
    while count_of_fives < n:
        current_num += 5
        count_of_fives += no_of_fives(current_num)
        print(current_num, count_of_fives)
    
    return current_num

findFactorial(6)