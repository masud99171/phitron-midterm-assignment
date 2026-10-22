class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


class Student:
    def __init__(self, student_id, name, department):
        self._studendid = student_id
        self.__name = name
        self.department = department
        self.is_enrolled = False
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.is_enrolled == False:
            self.is_enrolled = True
            print("enrol kora hoyeche")
            return True
        print("age thekei ache !")

    def drop_student(self):
        if self.is_enrolled == True:
            self.is_enrolled = False
            print("drop koraa hoyeche")
            return True
        print("age thekei nai !")

    def view_student_info(self):
        print(
            f"ID: {self._studendid} | Name: {self.__name} | Department: {self.department} | Enrolled: {self.is_enrolled}")

s0 = Student("101","ZulfiQar","Arabic")
s1 = Student("101", "Rakib Bhai", "CSE")
s2 = Student("102", "Hridoy Bhai", "EEE")
s3 = Student("103", "Sohel Bhai", "BBA")
s4 = Student("104", "Shaker", "Civil Engineering")
s5 = Student("105", "Ahad Bhai", "Arabic")
s6 = Student("106", "Asiq Bhai", "English")
s7 = Student("107", "Jhankar Bhai", "Computer Science")
s8 = Student("108", "Mentor Bhai", "Software Engineering")

while True:
    print("\n--- Student Management System ---")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = int(input("Enter your choice :"))
    if choice == 1:
        if len(StudentDatabase.student_list) == 0:
            print("ektao student nei")
        else:
            for s in StudentDatabase.student_list:
                Student.view_student_info(s)

    elif choice == 2:
        id = input("Enter Student ID: ")
        for i in StudentDatabase.student_list:
            if i._studendid == id:
                i.enroll_student()

    elif choice == 3:
        id = input("Enter Student ID: ")
        for i in StudentDatabase.student_list:
            if i._studendid == id:
                i.drop_student()

    elif choice == 4:
        print("program ses kora holo")
        break
    else:
        print("vul choice deoa hoyeche!")
