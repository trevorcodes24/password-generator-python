def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    print("Bubble Sort Program")
    user_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in user_input.strip().split()]
    
    print(f"Original list: {numbers}")
    bubble_sort(numbers)
    print(f"Sorted list: {numbers}")

if __name__ == "__main__":
    main()
