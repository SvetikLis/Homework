def sort_number():  # функция сортировки
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array


def binary_search(array, element, left, right):  # функция поиска
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


# ввод пользователем чисел с исключением ошибок
try:
    array = list(map(int, input("Введите числа через пробел: ").split()))
except ValueError as e:
    print("Введите целые числа")
    array = list(map(int, input("Введите числа через пробел: ").split()))

try:
    element = int(input("Введите целое чило для поиска: "))
except ValueError as e:
    print('Введите целое число')
    element = int(input("Введите целое чило для поиска: "))

print(sort_number())

try:
    x = binary_search(array, element, 0, len(array))
    if x not in array:
        print('Число', element, 'не в списке')
    else:
        print('Число', element, 'в списке с индексом', x, '\n', 'Индекс ближайшего элемента, который меньше =', x-1)
except IndexError as e:
    print('Число', element, 'больше любого числа из списка')