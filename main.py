numbers = input('Введите последовательность целых чисел через пробел: ')
num = int(input('Введите любое число: '))

def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

if " " not in numbers:
    print('Не введены пробелы!')
    numbers = input('Введите целые числа через пробел: ')
if not is_int(numbers):
    print('Введены некорректные данные. Программа завершена')
else:
    numbers = numbers.split()

list_of_numbers = [int(item) for item in numbers]

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


list_of_numbers = merge_sort(list_of_numbers)

def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'

print(f'Упорядоченный по возрастанию список: {list_of_numbers}')

if not binary_search(list_of_numbers, num, 0, len(list_of_numbers)):
    rI = min(list_of_numbers, key=lambda x: (abs(x - num), x))
    ind = list_of_numbers.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < num:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {list_of_numbers[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_of_numbers.index(rI)}
В списке нет меньшего элемента''')
    elif rI > num:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_of_numbers.index(rI)}
Ближайший меньший элемент: {list_of_numbers[min_ind]}, его индекс: {min_ind}''')
    elif list_of_numbers.index(rI) == 0:
        print(f'Индекс введенного элемента: {list_of_numbers.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(list_of_numbers, num, 0, len(list_of_numbers))}')
