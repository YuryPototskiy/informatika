numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# вычисляем сумму всех чисел, игнорируя None
total = sum(x for x in numbers if x is not None)
# общееколичество элементов в списке включая пропуск
count = len(numbers)
# среднее арифметическое
average = total / count

# заменяем первый встретившийся None на среднее значение
for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = average
        break

print("Измененный список:", numbers)
