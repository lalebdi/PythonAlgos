import self as self


class Person:
    name: str
    jon: str
    age: int

    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age


person1 = Person("Tony", "Iron Man", 30)
person2 = Person("Bruce", "Batman", 25)
person3 = Person("Bruce", "Batman", 25)

print(id(person2))
print(id(person3))
print(person1)

print(person3 == person2)