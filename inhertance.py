class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def is_annoying(self):
        print("annoying")


dog = Dog()
dog.walk()
dog.bark()

cat = Cat()
cat.walk()
cat.is_annoying()