data = input("Введите числа через пробел: ").split()
power = input("Введите степень: ")

if not power.isdigit():
    print("Ошибка: степень должна быть целым положительным числом.")
else:
    power = int(power)
    result = []

    for item in data:
        if item.isdigit() or (item.startswith("-") and item[1:].isdigit()):
            num = int(item)
            result.append(num**power)
        else:
            result.append(item * power)

    print("Вывод:", end=" ")
    print(" ".join(map(str, result)))
