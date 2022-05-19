"""Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний засіб".
Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель"."""

class Transport:
    first = 'car'
    second = 'aircraft'
    third = 'vessel'

class Car(Transport):
    color = 'red'

car = Car()
print('color of this', (car.first), 'is', (car.color))


class Aircraft(Transport):
    speed = 680

airplane = Aircraft()

print('speed of that', (airplane.second), 'is', (airplane.speed), 'km/h')


class Vessel(Transport):
    length = 180

ship = Vessel()

print('length of this', (ship.third), 'is', (ship.length), 'meters')



