def fib(n):
    if n==0 or n==1:
        return n
    ans = fib(n-1) + fib(n-2)
    return ans

n = int(input("Enter number to find Fibonacci Series -> "))
for i in range(n):
    print(fib(i))