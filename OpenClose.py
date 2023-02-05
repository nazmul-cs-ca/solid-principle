from abc import ABC, abstractmethod

class Person:
    classVariable: int = 10

    @staticmethod
    def Consumed():
        return Person.classVariable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self) -> str:
        return self.name

    def getAge(self) -> int:
        return self.age

    def __str__(self):
        return "Person:: name: {}, age: {}".format(self.name, self.age)

class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass

class PersonDatabase(PersonStorage):
    def __int__(self):
        pass

    def save(self, person):
        print("PersonDatabase save {}", str(person))

class PersonJSON(PersonStorage):
    def __int__(self):
        pass

    def save(self, person):
        print("PersonJSON:: save {}", str(person))

class PersonXML(PersonStorage):
    def __int__(self):
        pass

    def save(self, person):
        print("PersonXML:: save {}", str(person))



if __name__ == "__main__":
    print("hello from Single Responsibility!")
    person = Person("nazmul alam", 35)
    dbStorage = PersonDatabase()
    dbStorage.save(person)
