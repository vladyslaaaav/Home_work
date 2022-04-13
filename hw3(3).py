# Існує ліст з різними даними, lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть механізм, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні, які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

students = ['Steven', 23, 'David', 36, 'John', 19, 'Zelenskiy', 44]

for numeral in students:
    if type(numeral) == int:
        print('age:', numeral)







