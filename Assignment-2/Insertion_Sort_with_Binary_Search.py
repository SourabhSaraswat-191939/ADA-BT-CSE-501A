import time
import random

def binarySearch(arr, val, start, end):
    while start<=end:
        mid =  start + (end-start)//2
        if arr[mid]==val:
            return mid+1
        elif arr[mid]<val:
            start = mid+1
        else:
            end = mid-1
    return start

def insertionSort(arr):
    for i in range(1,len(arr)):     # we are starting from 1 as there is no sense to compare value at 0 index with none.
        val = arr[i]
        j = i-1
        search = binarySearch(arr,val, 0, j)
        while j>=search:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = val

    return arr

N = int(input("Enter the number of values you want to sort --> "))
numbers = []
for i in range(N):
    numbers.append(random.randint(0,N))

print(numbers)
start = time.time()
insertionSort(numbers)
end = time.time()
print(numbers)

print(f"Runtime of the program is {end - start}")

# Time Complexity (Worst Case): O(n^2)
# Still the time complexity is same due to number of swaps are still same. We only decreased the number of comparison. So, time taken to sort will decrease not time complexity.
# Time Complexity (Best Case): O(n) 
