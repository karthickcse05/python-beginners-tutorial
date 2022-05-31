class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi {self.name}")

person = Person("MS Dhoni")
person.talk()

person1 = Person("Rohit Sharma")
person1.talk()