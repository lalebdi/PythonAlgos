from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)  # Freezing means creating objects that are read only
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str  # Datatype is important if using dataclass
    job: str
    age: int
    strength: int = 100

    # Constructor is no longer needed since we are using dataclass
    # def __init__(self, name, job, age):
    #     self.name = name
    #     self.job = job
    #     self.age = age

    def __post_init__(self):  # For the sorting index
        # self.sort_index = self.age
        object.__setattr__(self, 'sort_index', self.age)

    def __str__(self):
        return f"{self.name}, {self.job} ({self.age})"


person1 = Person("Tony", "Iron Man", 30)
person2 = Person("Bruce", "Batman", 25, 99)
person3 = Person("Bruce", "Batman", 25, 99)

print(id(person2))
print(id(person3))
print(person1)

print(person3 == person2)
print(person3 > person2)
