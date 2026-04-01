class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    def say_hello(self):
        print(f"Hello my name is {self.name} and i am {self._age} years old")
    

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id

    def say_hello(self):
        super().say_hello()
        print(f"My student ID is {self.__student_id}.")

    def get_student_id(self):
        return self.__student_id
    def __del__(self):
        print("Student destructor called")
W = Person("Wataru", 19)
W.say_hello()

Ws = Student("Wataru", 19, 25112007)
Ws.say_hello()


print(W.name)

print(Ws.get_student_id())

del Ws
