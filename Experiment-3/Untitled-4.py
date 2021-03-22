class Animal:
    def show(self):
        pass


class Cat(Animal):
    def show(self):
        return super().show()


class Dog(Animal):
    def show(self):
        return super().show()


class Tiger(Animal):
    def show(self):
        return super().show()


cat = Cat()
dog = Dog()
tiger = Tiger()
cat.show()
dog.show()
tiger.show()
