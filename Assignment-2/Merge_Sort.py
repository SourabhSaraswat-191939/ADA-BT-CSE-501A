import time, random, sys
sys.setrecursionlimit(3010)

def MergeSort(arr):
    length = len(arr)
    result = []
    if length>1:
        mid = length//2
        left = MergeSort(arr[:mid])
        right = MergeSort(arr[mid:])
        i=0
        j=0
        while i<len(left) or j<len(right):
            if i==len(left):
                result +=right[j:]
                break
            elif j==len(right):
                result +=left[i:]
                break
            else:
                if left[i]>=right[j]:
                    result.append(right[j])
                    j+=1
                else:
                    result.append(left[i])
                    i+=1
        return result
    return arr
            
n = int(input("Enter the number of values you want to sort --> "))
numbers = []
for _ in range(n):
    numbers.append(random.randint(0,n))
print(numbers)
start = time.time()
numbers = MergeSort(numbers)
end = time.time()
print(numbers)
print(f"Runtime of the program is {end - start}")
