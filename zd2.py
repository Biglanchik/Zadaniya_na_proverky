num = input("Введите число: ")

is_number = True
for ch in num:
    if ch not in "0123456789":
        is_number = False
        break

if is_number and num != "":
    num = int(num)
    if num > 0 and num % 2 == 0:
        print("Число чётное")
    else:
        print("Число нечётное")
else:
    print("Введено не число")
