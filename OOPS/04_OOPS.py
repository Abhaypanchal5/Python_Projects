class Animal:
    def __init__(self,name,species):
        self.name = name
        self.spe = species
    
    def speak(self):
        print(f"{self.name} makes a sound")
        
    def display(self):
        print(f"Name : {self.name}\nSpecies : {self.spe}")
        
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")
        
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")
        
cat = Cat('XYZ','ABC')
cat.speak()
cat.display()

dog = Dog('XYZ','ABC')
dog.speak()
dog.display()