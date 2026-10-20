class Student:
    def __init__(self, name, id, grade):
        self.name=name
        self.id= id
        self.grade=grade

    def show_info(self):
        print("name:", self.name)
        print("id:", self.id)
        print("grade:", self.grade)

C_1= Student("Mohamed", 202501202, 90)
C_1.show_info()    