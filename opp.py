class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pr(self):
        print(self.name, self.age)


class Man(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def pr(self):
        print(self.name)


v = Man("Vasya", 25)





