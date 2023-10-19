# 
class Person ():
    def show_details(self):
        return f"Running from {self.__class__.__name__} class"
    
person = Person()

print(person.show_details())

print ("----")

# dekorator @classmethod
class Container ():

    @classmethod
    def show_details(cls):
        return f"Running from {cls.__name__} class."
    
print(Container.show_details())

print ("----")

# dekorator @classmethod
class Counter():

    instances = []

    def __init__(self, counter) -> None:
        self.counter = counter
        Counter.instances.append(self)

    @classmethod
    def count_instances(cls):
        return len (cls.instances)

 
oneNumber = Counter('1')
twoNumber = Counter('2')
threeNumber = Counter('3')

print(Counter.count_instances())

print ("----")