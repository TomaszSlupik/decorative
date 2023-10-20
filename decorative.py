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

# classmethod - kolejny przykład 
class Worker ():
    list_worker = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Worker.list_worker.append(self)

    @classmethod
    def count_instances(cls):
        return len(cls.list_worker)
    
firstWorker = Worker('Jan', 'Kowalski')
secondWorker = Worker('Emil', 'Konder')

print(Worker.count_instances())

print ("----")

# @staticmethod - dekorator 
import time 

class Container ():

    @staticmethod
    def get_current_time():
        return time.strftime('%H:%M:%S', time.localtime())
    
print (Container.get_current_time())

print ("----")

# staticmethod - dekorator
import uuid

class Book ():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_id = self.get_id()

    @staticmethod
    def get_id():
        book_id = str(uuid.uuid4().fields[-1])[:6]
        return book_id
    
book1 = Book('Inferno', 'Dan Brown')

print(book1.__dict__.keys())

print ("----")

# staticmethod - dekorator
class Phone():

    def __init__(self, brand, price):
        self.brand = brand 
        self.price = price 
        self.phone_id = self.get_id()

    @staticmethod
    def get_id():
        phone_id = str(uuid.uuid4().fields[-1])[:6]
        return phone_id

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: \n Marka: {self.brand} \n Cena: {self.price} zł \n ID_telefonu: {self.get_id()}"
    
onePhone = Phone('Iphone', 6000)
print(onePhone)

print ("----")
