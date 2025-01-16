#Karlo Robert C. Wagan
#BSCS - 3
#ITP 6 - Algorithm And Complexity

import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Swapped {arr[i]} with {arr[min_index]}: {arr}")
        time.sleep(0.1)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f"Swapped {arr[j]} with {arr[j+1]}: {arr}")
                time.sleep(0.1)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            print(f"Moved {arr[j+1]} to position {j+2}: {arr}")
            time.sleep(0.1)
        arr[j + 1] = key
        print(f"Inserted {key} at position {j+1}: {arr}")
        time.sleep(0.1)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print(f"Merged: {arr}")
        time.sleep(0.1)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"Swapped {arr[i]} and {arr[j]}: {arr}")
    arr[i+1], arr[high] = arr[high], arr[i+1]
    print(f"Moved pivot {arr[i+1]} to correct position: {arr}")
    time.sleep(0.1)
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print(f"Partitioned at index {pi}: {arr}")
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
        time.sleep(0.1)

def generate_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def main():
    print("Sorting Algorithm Simulator")
    size = int(input("Enter the size of the list: "))
    lower_bound = int(input("Enter the lower bound of the list values: "))
    upper_bound = int(input("Enter the upper bound of the list values: "))
    
    arr = generate_random_list(size, lower_bound, upper_bound)
    print(f"Generated list: {arr}")
    
    print("Choose sorting algorithm:")
    print("1. Selection Sort")
    print("2. Bubble Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    choice = int(input("Enter your choice (1/2/3/4/5): "))
    
    if choice == 1:
        print("Performing Selection Sort...")
        selection_sort(arr)
    elif choice == 2:
        print("Performing Bubble Sort...")
        bubble_sort(arr)
    elif choice == 3:
        print("Performing Insertion Sort...")
        insertion_sort(arr)
    elif choice == 4:
        print("Performing Merge Sort...")
        merge_sort(arr)
    elif choice == 5:
        print("Performing Quick Sort...")
        quick_sort(arr, 0, len(arr)-1)
    else:
        print("Invalid choice!")

    print(f"Sorted list: {arr}")

if __name__ == "__main__":
    main()