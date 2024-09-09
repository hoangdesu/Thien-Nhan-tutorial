# def fib(elements) -> int[]:
#     ...
    
# fib(5) -> [0, 1, 1, 2, 3]
# fib(10) -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    

# Recusive function: function calling itself

# base case: stop the function

def count(n):
    # base case
    if (n == 10):
        return
    
    print(n)
    count(n + 1)

count(1)

# 26/02/1995 
# 2+6+2+1+9+9+5=34
# 3+4=7

# 10/15/2008
# 17
# => 8

def calculateNumerology(dob):
    return int

# calculateNumerology('10/15/2008') -> 8