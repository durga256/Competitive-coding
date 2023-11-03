#Find factorial of a large number
def factorial(N):
 
    # Initialize result
    f =  1 
     
    # Multiply f with 2, 3, ...N
    for i in range(2, N + 1):
        f *= i
     
    return f
 
 
# Driver method
N = 20
print(factorial(N))