# Animal is-a object (yes, sort of confusing) look ath the extra credit
class Animal(object):
    pass

# Dog is-an Animal


class Dog(Animal):
    def __init__(self, name):
        # Dog has-a name
        self.name = name

# Cat is-an Animal


class Cat(Animal):
    def __init__(self, name):
        # Cat has-a name
        self.name = name

# Person is-a object


class Person(object):
    def __init__(self, name):
        # Person has-a init
        self.name = name
        # Person has-a pet of some kind
        self.pet = None

# Employee is-a Person


class Employee(Person):
    def __init__(self, name, salary):
        # Person has-a init with parameter self, name, salary
        super(Employee, self).__init__(name)
        # Person has-a salary
        self.salary = salary

# Fish is-a object


class Fish(object):
    pass

# Salmon is-a Fish


class Salmon(Fish):
    pass

# Halibut is-a fish


class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a person
mary = Person("Mary")

# mary has-a pet name satan
mary.pet = satan

# frank is-a Employee. Frank has-a name Frank and salary 1200000
frank = Employee("Frank", 120000)

# frank has-a pet rover
frank.pet = rover

# flipper is-a fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
