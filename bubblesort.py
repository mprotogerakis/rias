from typing import List

def bubble_sort(arr: List[int]) -> None:
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Beispielaufruf
arr: List[int] = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sortierte Liste:")
for element in arr:
    print(element)