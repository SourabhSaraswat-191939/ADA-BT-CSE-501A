import time

n = int(input("Enter number to find Fibonacci Series -> "))

# creating a variable to store data of calculated terms, so that we can use dynamic programming approach.
Dp_arr = [-1]*(n+1)
Dp_arr[0] = 0   # as 1st term of fibonacci is 0.
Dp_arr[1] = 1   # as 2nd term of fibonacci is 1.

# using time library to record the start time.
start = time.time()   
for i in range(2,n+1):
    Dp_arr[i] = Dp_arr[i-1] + Dp_arr[i-2]

# using time library to record the end time.
end = time.time()

# printing n terms of fabonacci series.
print(Dp_arr)
print(f"Runtime of the program is {end - start} seconds")