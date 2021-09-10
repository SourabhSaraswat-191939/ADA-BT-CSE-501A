Dp_arr = [-1]*(10+1)
def fib(n):
    Dp_arr[0] = 0
    Dp_arr[1] = 1
    for i in range(2,n+1):
        Dp_arr[i] = Dp_arr[i-1] + Dp_arr[i-2]
    return Dp_arr[n]


n = int(input("Enter number to find Fibonacci Series -> "))
fib(n)

print(Dp_arr)