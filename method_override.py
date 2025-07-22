name = input("Enter the name of the person: ")
age = int(input("Enter the age of the person: "))
hair_colour = input("Enter the hair colour of the person: ")
eye_colour = input("Enter the eye colour of the person: ")


# The parent class
class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    # The function gets called by the object if the user is old enough to drive
    def can_drive(self):
        return self.name + " is old enough to drive."


# Subclass of the "adult" parent class
class Child(Adult):
    def __init__(self, name, age, hair_colour, eye_colour):
        super().__init__(name, age, hair_colour, eye_colour)

    # The function gets called by the object if
    # the user is not old enough to drive
    def can_drive(self):
        # code that the person is young to drive
        return self.name + " is too young to drive."


if age >= 18:
    person = Adult(name, age, hair_colour, eye_colour)
    print(person.can_drive())
else:
    person = Child(name, age, hair_colour, eye_colour)
    print(person.can_drive())