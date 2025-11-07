class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):     # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name)  # inherit name from Animal
        self.breed = breed      # Dog-specific attribute

    def speak(self):            # override method
        print(f"{self.name} the {self.breed} barks")


# Create objects
animal = Animal("Generic Animal")
dog = Dog("Buddy", "Golden Retriever")

animal.speak()
dog.speak()


# You successfully created classes (Animal, Dog)

# You used inheritance (Dog inherited from Animal)

# You used method overriding (speak() is redefined in Dog)

# You instantiated objects (animal and dog)