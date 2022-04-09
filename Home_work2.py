age = 7
age2 = 16
age3 = 65

while True:
    guess = int(input('Скільки тобі років?'))
    
    if guess < age:
        print('Де твої батьки?')
    elif guess < age2:
        print('Це фільм для дорослих!')
    elif guess > age3:
        print('Покажіть пенсійне посвідчення!')
    else:
        if (guess / 11) % 1 == 0:
            print('Який цікавий у вас вік!')
        else:
            print('Білетів вже немає!') 
    