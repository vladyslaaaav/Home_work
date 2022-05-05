age = ['років', 'роки', 'рік']

def Vlad():

    """
Попросіть користувача ввести свій вік.

- якщо користувачу менше 7 - вивести 'Тобі ж <>! Де твої батьки?'
- у будь-якому іншому випадку - вивести 'Незважаючи на те, що вам <>, білетів всеодно нема!' """

    try:
        cashier = int(input('Скільки тобі років?'))
    except:
        print('Я вас не розумію')
    else:
        if cashier == 1:
            print('Тобі всього', cashier, age[2], 'Де твої батьки?')
        elif 4 >= cashier >= 2:
            print('Тобі всього', cashier, age[1], 'Де твої батьки?')
        elif 7 >= cashier >= 5:
            print('Тобі всього', cashier, age[0], 'Де твої батьки?')
        else:
            print('Незважаючи на те, що вам', cashier, ',білетів вже немає')
Vlad()


def Bob():
    """Попросіть користувача ввести свій вік.
    - якщо користувачу менше 16 - вивести 'Тобі лише <>, а це е фільм для дорослих!'
    - у будь-якому іншому випадку - вивести 'Незважаючи на те, що вам <>, білетів всеодно нема!' """

    try:
        cashier = int(input('Скільки тобі років?'))
    except:
        print('Я вас не розумію')
    else:
        if 16 > cashier >= 7:
            print('Тобі лише', cashier, age[0], 'Цей фільм для дорослих!')
        else:
            print('Незважаючи на те, що вам', cashier, ',білетів вже немає')
Bob()


def Polina():
    """Попросіть користувача ввести свій вік.
    - якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
    - у будь-якому іншому випадку - вивести 'Незважаючи на те, що вам <>, білетів всеодно нема!'"""

    try:
        cashier = int(input('Скільки тобі років?'))
    except:
        print('Я вас не розумію')
    else:
        if cashier > 65 and cashier % 10 in (2, 3, 4):
            print('Вам', cashier, age[1], '? ваше посвідчення, будь ласка!')
        elif cashier > 65 and cashier % 10 in (5, 6, 7, 9, 0):
            print('Вам', cashier, age[0], '? ваше посвідчення, будь ласка!')
        elif cashier > 65 and cashier % 10 in (1):
            print('Вам', cashier, age[2], '? ваше посвідчення, будь ласка!')
        elif cashier > 65 and cashier % 10 in (11, 12, 13, 14):
            print('Вам', cashier, age[0], '? ваше посвідчення, будь ласка!')
        else:
            print('Незважаючи на те, що вам', cashier, ',білетів вже немає')
Polina()

def John():
    """Попросіть користувача ввести свій вік.
    - якщо вік користувача складається з однакових цифр
    (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "О, вам <>! Який цікавий вік!"
    - у будь-якому іншому випадку - вивести 'Незважаючи на те, що вам <>, білетів всеодно нема!'"""

    try:
        cashier = int(input('Скільки тобі років?'))
    except:
        print('Я вас не розумію')
    else:
        if cashier % 11 == 0:
            print('О,вам', cashier, '! який цікавий у вас вік!')
        else:
            print('Незважаючи на те, що вам', cashier, ',білетів вже немає')
John()