age = 7
age2 = 16
age3 = 65

while True:
    guess = int(input('Скільки тобі років?'))
    if (guess / 11) % 1 == 0:
        print('Цікавий в тебе вік')
    else:
        if guess < age:
            print('Де твої батьки?')
        elif guess < age2:
            print('Цей фільм для дорослих')
        elif guess > age3:
            print('Посвідчення')
        else:
            print('А білетів вже немає!')