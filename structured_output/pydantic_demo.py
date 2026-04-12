from pydantic import BaseModel

class Student(BaseModel):

    name: str
    age: int

new_student = {'name':'samarpan','age':'32'} #even though i pass string here, pydantic automatically converts into int. But if i pass 'abc' it cant convert into int. This is type coercing

student = Student(**new_student) # ** unpacks the dictionary into keyword arguments

print(student)