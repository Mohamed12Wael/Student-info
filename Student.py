class Student:
    def __init__(self, name, id, grade):
        self.name=name
        self.id= id
        self.grade=grade

    def display_info(self):
        print("name:", self.name)
        print("id:", self.id)
        print("grade:", self.grade)


class UndergraduateStudent(Student):
    def __init__(self, name, id, grade, major):
        super().__init__(name, id, grade)
        self.major=major


    def display_info(self):
        super().display_info()
        print("Major:",self.major)


class  GraduateStudent(Student):
    def __init__(self, name, id, grade, program_title):
        super().__init__(name, id, grade)
        self.program_title=program_title

    def display_info(self):
        super().display_info()
        print("program_title:",self.program_title)

C_1= Student("Mohamed", 202501202, 90)
C_1.display_info()   
u1= UndergraduateStudent("Hoksha", 333, 40, "EEE")
u1.display_info()
g1 = GraduateStudent("Sara", 202, 85, "MSc Robotics")
g1.display_info()