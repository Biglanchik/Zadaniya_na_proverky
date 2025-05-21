dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

keys_set = set()
values_set = set()

for key in dct:
    keys_set.add(key)
    values_set.add(dct[key])

union_set = keys_set.union(values_set)

print("Множество ключей:", keys_set)
print("Множество значений:", values_set)
print("Объединение множеств:", union_set)
