class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof")

dog1 = Dog()

dog1.speak()