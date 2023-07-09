def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1

def sort_list(arr):
    return sorted(arr)

sequence = input("Введите последовательность чисел через пробел: ")
try:
    sequence = list(map(int, sequence.split()))
except ValueError:
    print("Ошибка ввода данных")
    exit()

number = input("Введите число: ")
try:
    number = int(number)
except ValueError:
    print("Ошибка ввода данных")
    exit()

sorted_sequence = sort_list(sequence)
position = binary_search(sorted_sequence, number)

if position == -1:
    print("Введенное число не найдено в последовательности")
else:
    print("Позиция элемента:", position)