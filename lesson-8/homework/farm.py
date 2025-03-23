class MilkProducer:
    def __init__(self, milk_production):
        self.milk_production = milk_production  # liters per day

    def produce_milk(self):
        return self.milk_production

class EggLayer:
    def __init__(self, egg_production):
        self.egg_production = egg_production  # eggs per week

    def lay_eggs(self):
        return self.egg_production

class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Cow(Animal, MilkProducer):
    def __init__(self, name, age, weight, milk_production):
        Animal.__init__(self, name, age, weight)
        MilkProducer.__init__(self, milk_production)

    def make_sound(self):
        return "Moo"

class Chicken(Animal, EggLayer):
    def __init__(self, name, age, weight, egg_production):
        Animal.__init__(self, name, age, weight)
        EggLayer.__init__(self, egg_production)

    def make_sound(self):
        return "Cluck"

class Pig(Animal):
    def __init__(self, name, age, weight, weight_gain):
        super().__init__(name, age, weight)
        self.weight_gain = weight_gain

    def make_sound(self):
        return "Oink"

    def gain_weight(self):
        self.weight += self.weight_gain
        return f"{self.name} has gained {self.weight_gain} kg. New weight is {self.weight} kg."

class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def view_animals(self):
        for animal in self.animals:
            print(f"{animal.name} (Age: {animal.age}, Weight: {animal.weight} kg) - {animal.make_sound()}")

    def total_milk_production(self):
        return sum(animal.produce_milk() for animal in self.animals if isinstance(animal, MilkProducer))

    def total_egg_production(self):
        return sum(animal.lay_eggs() for animal in self.animals if isinstance(animal, EggLayer))

# Example Usage
if __name__ == "__main__":
    farm = Farm()
    
    bessie = Cow("Bessie", 5, 600, 25)
    clucky = Chicken("Clucky", 2, 2, 7)
    porky = Pig("Porky", 3, 150, 5)

    farm.add_animal(bessie)
    farm.add_animal(clucky)
    farm.add_animal(porky)

    farm.view_animals()
    print(f"Total milk production: {farm.total_milk_production()} liters per day.")
    print(f"Total egg production: {farm.total_egg_production()} eggs per week.")