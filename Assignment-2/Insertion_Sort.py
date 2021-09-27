#Insertion sort is used when number of elements is small. It can also be useful when input array 
# is almost sorted, only few elements are misplaced in complete big array.
import time, random, sys
sys.setrecursionlimit(3010)

def insertionSortRecur(arr,n):
    if n<=1:
        return
    
    insertionSortRecur(arr,n-1)
    val = arr[n-1]
    j = n-2
    while j>=0 and val<arr[j]: #compare value with its predecissors till we get the right position.
        arr[j+1] = arr[j]      # performing swap here.
        j-=1
    arr[j+1] = val          # placing the value at right position.

    return arr

def insertionSort(arr):
    # we are starting from 1 because there is no sense to compare value at 0 index with none.
    for i in range(1,len(arr)):     
        val = arr[i]
        j = i-1
        while j>=0 and val<arr[j]: #compare value with its predecissors till we get the right position.
            arr[j+1] = arr[j]      # performing swap here.
            j-=1
        arr[j+1] = val          # placing the value at right position.

    return arr

N = int(input("Enter the number of values you want to sort --> "))
numbers = []
for i in range(N):
    numbers.append(random.randint(0,N))

print(numbers)
start = time.time()
numbers = insertionSortRecur(numbers,N)
end = time.time()
print(numbers)

print(f"Runtime of the program is {end - start}")

# Time Complexity (Worst Case): O(n^2) 
# Time Complexity (Best Case): O(n) 


# Number of comparisons in Normal Insertion sort can be decreased by using Binary Search.
# Insertion sort takes "n" comaprisons for "n-th interation" in worst case.
# With the use of Binary Search with Insertion Sort, we can decrease comparison for "n-th interation" to "log(n)" in worst case.
