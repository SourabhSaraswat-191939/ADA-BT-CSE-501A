import time

n = int(input("Enter number to find Fibonacci Series -> "))

Dp_arr = [-1]*(n+1)
Dp_arr[0] = 0
Dp_arr[1] = 1

start = time.time()
for i in range(2,n+1):
    Dp_arr[i] = Dp_arr[i-1] + Dp_arr[i-2]

end = time.time()

print(Dp_arr)
print(f"Runtime of the program is {end - start} seconds")