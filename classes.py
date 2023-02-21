class Pet:
    # use the keyword class and a capitalized word to define a class
    # classes are like blueprints for making specialized objects

    # every class has a __ init method, that causes an instance (individual item of) the class to be made, using the blueprint
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # instance methods are actions that can be performed on or by an instance of the class

    def call(self):
        # self refers to the specific instance of Pet that you are calling
        print(f'Come here, {self.name}!')


class Person:
    def __init__(self, provided_name='anonymous', provided_age=None):
        # giving the parameters default values also turns them into
        # keyword arguments
        self.name = provided_name
        self.age = provided_age

    def greet(self):
        print("Hello, {self.name}")


# Example, create a Person record for Rihanna
riri = Person(provided_age=32, provided_name="Rihanna")
# with keyword arguments, the order you pass them does not matter
backup_dancer1 = Person(provided_age=24)
# because we gave default values to the arguments, they are not required
backup_dancer1.name = "Christina"
# we can update the value if the data
