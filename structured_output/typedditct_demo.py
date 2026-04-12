from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person : Person= {'name':'samarpan', 'age': 18}
print(new_person)

#TypedDict doesnt validate the values. so even if we give a string value to age, it works
new_person : Person= {'name':'aastha', 'age': '16'}
print(new_person)