class Dog:

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

Dog1 = Dog("Golden Retriever", 'Yellow')

Dog2 = Dog("Shih Tzu", 'White')

print("Hello, I am a {}".format(Dog1.name))
print( "I am {}.".format(Dog1.colour))

print("Hello, I am a {}".format(Dog2.name))
print( "I am {}.".format(Dog2.colour))
