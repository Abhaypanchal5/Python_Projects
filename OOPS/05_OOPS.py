class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
        
    def speak(self):
        print(f'{self.name} make a sound')
        
    def display_info(self):
        print(f'Name : {self.name}\nSpecies : {self.species}')
        

class Cat(Animal):
    def __init__(self, name, species,colour):
        super().__init__(name, species)
        self.colour = colour
        
    def speak(self):
        print(f'{self.name} says Meow!!')   
        
    def show_colour(self):
        print(self.colour)
        
cat1 = Cat('XYZ','ABC','Black')

cat1.show_colour()
cat1.speak()
cat1.display_info()