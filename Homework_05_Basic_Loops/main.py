from math import sqrt


def isPrime(n):
    if n == 2:
        return True
    elif n < 1 or not n % 2:
        return False
    for i in range(3, int(sqrt(n) + 1), 2):
        if not n % i:
            return False
    else:
        return True




for i in range(1, 101):

    if not i % 3 and not i % 5 and isPrime(i):
        print(f"{i} - FizzBuzz and Prime number")
    
    elif not i % 3 and not i % 5:
        print(f"{i} - FizzBuzz")
    
    elif not i % 3 and isPrime(i):
        print(f"{i} - Fizz and Prime number")
    
    elif not i % 3:
        print(f"{i} - Fizz")
    
    elif not i % 5 and isPrime(i):
        print(f"{i} - Buzz and Prime number")
    
    elif not i % 5:
        print(f"{i} - Buzz")
    
    elif isPrime(i):
        print(f"{i} - Prime number")    
    
    else:
        print(i)

    