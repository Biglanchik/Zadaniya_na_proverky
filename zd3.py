age = input("Введите ваш возраст: ")

is_number = True
for ch in age:
    if ch not in "0123456789-":
        is_number = False
        break

if not is_number or age == "":
    print("Введено не число!")
else:
    age = int(age)
    if age < 0:
        print("Возраст не может быть отрицательным!")
    else:
        if age >= 18:
            print("Вы совершеннолетний.")
        else:
            print("Вы несовершеннолетний.")
