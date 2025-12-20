# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Animal Name: {self.name}")


# Mammal Class
class Mammal(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature

    def show_feature(self):
        print(f"Mammal Feature: {self.feature}")


# Bird Class
class Bird(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature

    def show_feature(self):
        print(f"Bird Feature: {self.feature}")


# Fish Class
class Fish(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature

    def show_feature(self):
        print(f"Fish Feature: {self.feature}")


# ----- Mammal Children -----
class Dog(Mammal):
    def walk(self):
        print(f"{self.name} is walking 🐕")


class Cat(Mammal):
    def walk(self):
        print(f"{self.name} is walking 🐈")


# ----- Bird Children -----
class Eagle(Bird):
    def fly(self):
        print(f"{self.name} is flying 🦅")


class Penguin(Bird):
    def swim(self):
        print(f"{self.name} is swimming 🐧")


# ----- Fish Children -----
class Salmon(Fish):
    def swim(self):
        print(f"{self.name} is swimming 🐟")


class Shark(Fish):
    def swim(self):
        print(f"{self.name} is swimming 🦈")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    dog = Dog("Buddy", "Has fur")
    dog.show_name()
    dog.show_feature()
    dog.walk()

    print("------------")

    eagle = Eagle("Rocky", "Has wings")
    eagle.show_name()
    eagle.show_feature()
    eagle.fly()

    print("------------")

    shark = Shark("Great White", "Lives in water")
    shark.show_name()
    shark.show_feature()
    shark.swim()
