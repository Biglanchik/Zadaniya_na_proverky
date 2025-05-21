list1 = input("Введите первый список: ").split()
list2 = input("Введите второй список: ").split()

set1 = set(list1)
set2 = set(list2)

common_elements = set1 & set2  

print("Общие элементы:", ' '.join(common_elements))