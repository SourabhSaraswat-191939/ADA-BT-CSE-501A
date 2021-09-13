import time

def fib(n):
    if n==0 or n==1:
        return n
    ans = fib(n-1) + fib(n-2)   # using recursion here
    return ans

n = int(input("Enter number to find Fibonacci Series -> "))

# using time library to record the start time.
start = time.time()
for i in range(n):
    print(fib(i))   # printing n terms of fabonacci series one by one using for loop.

# using time library to record the end time.
end = time.time()

print(f"Runtime of the program is {end - start} seconds")