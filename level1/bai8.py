class Person:
    name = "Hjn4"

    def __init__(self, name_from_user=None):
        self.name = name_from_user


changme = Person("Trang My")
print(changme.name)

huyna = Person()
print(huyna.name)
huyna.name = "HJN4"

print(f"{Person.name} is {huyna.name}")
