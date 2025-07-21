"""
Compulsory Task 1:
------------------

"""


# Parent class
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def location(self):
        head_office_location = "Cape Town" 


# child class
class OOPCourse(Course):
    def __init__(self, description, trainer):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        print(self.description)
        print(self.trainer)

    def show_course_id(self):
        id_number = "#12345"
        print(id_number)

course_1 = OOPCourse("computer science", "Guido Van Rossum:")

course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
