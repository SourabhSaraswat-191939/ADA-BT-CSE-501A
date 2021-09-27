import time, random, sys
sys.setrecursionlimit(3010)

def BubbleSortRecur(arr,n):
    if n == 1:
        return
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]   # Performing swap between arr[i] and arr[i+1]
            
    BubbleSortRecur(arr,n-1)      
    return arr

def BubbleSort(arr,n):
    while True:         # Run this while loop till we get the sorted array
        count = 0       # To count how many elements are not at their sorted position.
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]   # Performing swap between arr[i] and arr[i+1]
                count=1
        # If count=0 then all elements are at their sorted position, so we can break loop.
        if count==0:  
            break
    return arr

n = int(input("Enter the number of values you want to sort --> "))
numbers = []
for _ in range(n):
    numbers.append(random.randint(0,n))
print(numbers)
start = time.time()  # using time library to record the start time.
numbers = BubbleSortRecur(numbers,n)
end = time.time()    # using time library to record the end time.
print(numbers)
print(f"Runtime of the program is {end - start}")
