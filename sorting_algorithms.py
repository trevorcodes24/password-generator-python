def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    print("Sorting Program")
    algo = input("Choose sorting algorithm (bubble/insertion): ").strip().lower()
    user_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in user_input.strip().split()]

    if algo == "bubble":
        bubble_sort(numbers)
    elif algo == "insertion":
        insertion_sort(numbers)
    else:
        print("Invalid choice.")
        return

    print(f"Sorted list: {numbers}")

main()