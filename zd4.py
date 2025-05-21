while True:
    num = input("Введите число: ")

    if num == "exit":
        print("Выход из программы...")
        break

    if not num.lstrip("-").isdigit():
        print("Данные не являются числом.")
        continue

    digits = len(num.lstrip("-"))
    print(f"В этом числе {digits} цифры.")
