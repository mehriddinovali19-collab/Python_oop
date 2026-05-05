from datetime import datetime


class Person:

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age
        self.created_at = datetime.today()


p01 = Person('ali', 'valeyiv', 13)
p02 = Person('vali', 'oybekov', 18)
p03 = Person('guli', 'asaliva', 29)


print(p01.first_name, p01.last_name, p01.age, p01.created_at)
print(p02.first_name, p02.last_name, p02.age, p02.created_at)
print(p03.first_name, p03.last_name, p03.age, p03.created_at)