class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"
    

class JackRusselTerrier(Dog):
    def speak(self, sound='Arf'):
        return super().speak(sound)

class Danchshud(Dog):
    pass

class Bulldog(Dog):
    pass

