class Transport:
    color = 'red'
    color2 = 'white'
    color3 = 'black'

    def __int__(self, initial_color, initial_color2, initial_color3):
        self.color = initial_color
        self.color2 = initial_color2
        self.color3 = initial_color3

    def colors(self):
        return f'I have {self.color} car, {self.color2} aircraft and {self.color3} vessel'

class Car(Transport):
    tone = 'dark'

car1 = Car(initial_color='blue')

print(car1.colors())

