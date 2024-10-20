class Animal:
    def __init__(self,name,age,habitant,is_available):
        self.name = name
        self.age = age
        self.habitant = habitant
        self.is_available = is_available

    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Habitant: {self.habitant}, Available Status: {self.is_available}"

    def change_availability(self, status):
        self.is_available = status

class Mammal(Animal):
    furlength = 0
    diet = ''
    def __init__(self, name, age, habitant,is_available,furLength,diet):
        super().__init__(name, age, habitant,is_available)
        self.furLength = furLength
        self.diet = diet

    def show(self):
        info = super().show()
        return f"{info}, Fur Length: {self.furLength}, Diet: {self.diet}"

class Bird(Animal):
    def __init__(self, name, age, habitant, is_available,wingspan,flight_altitude):
        super().__init__(name, age, habitant, is_available)
        self.wingspan = wingspan
        self.flight_altitude = flight_altitude

    def show(self):
        info = super().show()
        return f"{info}, Wingspan: {self.wingspan}, Flight Altitude: {self.flight_altitude}"


class Reptile(Animal):
    def __init__(self, name, age, habitant, is_available,scale_pattern,is_venomous):
        super().__init__(name, age, habitant, is_available)
        self.scale_pattern = scale_pattern
        self.is_venomous = is_venomous

    def show(self):
        self.info = super().show()
        return f"{self.info}, Scale Pattern: {self.scale_pattern}, Venomous: {self.is_venomous}"


lion = Mammal("Lion", 5, "Africa", True, 10, "Carnivore")
eagle = Bird("Eagle", 3, "Mountains", True, 2.1, 3000)
snake = Reptile("Snake", 2, "Jungle", False, "Smooth", True)

print(lion.show())
print(eagle.show())
print(snake.show())

snake.change_availability(True)

print(snake.show())
