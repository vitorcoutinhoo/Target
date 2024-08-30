# Questão 2

def Fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)

def isFibonacci(n):
    i = 0
    while True:
        if Fib(i) == n:
            return True
        
        if Fib(i) > n:
            return False

        i += 1

num = 4
resp = isFibonacci(num)

if resp:
    print(f"O número {num} pertence à sequência de Fibonacci")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci")
    
    

    
    
    