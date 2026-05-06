from datetime import datetime

class Person:

    def __init__(self, first_name: str, last_name: str, birth_year: int):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year   # FIX

    @property
    def age(self) -> int:
        return self.get_current_year() - self.birth_year
    
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    @staticmethod
    def get_current_year() -> int:
        return datetime.today().year
    
    def to_dict(self) -> dict:
        return {
            "first name": self.first_name,
            "last name": self.last_name,
            "full name": self.full_name,
            "age": self.age
        }
    
    @classmethod   # FIX
    def from_dict(cls, data: dict):
        return cls(data['first_name'], data['last_name'], data['birth_year'])
    

data = {"first_name": "ali", "last_name": "valiyev", "birth_year": 2008}
p01 = Person.from_dict(data)

print(p01.to_dict())