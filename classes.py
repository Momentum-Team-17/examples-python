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
