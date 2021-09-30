class Dog:
    # class variables are shared amongst all instances
    #tricks = [] # mistaken use of a class variable

    def __init__(self, name):
        self.name = name
        self.tricks = []
    
    def add_trick(self, trick):
        self.tricks.append(trick) # instance variable is correct use in this case

    def __str__(self):
        return f'{self.name} learned {self.tricks}'

x = Dog("Bogart")
x.add_trick("Fetch")
print(x)