class InvalidMarksError(Exception):
    pass

class Student:
    def __init__(self, name, register_no, marks):
        self.name = name
        self.register_no = register_no
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return "Name: " + self.name + "\nRegister Number: " + self.register_no


try:
    name = input("Enter student name: ")
    register_no = input("Enter register number: ")

    marks = []

    for i in range(5):
        mark = int(input("Enter marks for subject " + str(i + 1) + ": "))

        if mark < 0 or mark > 100:
            raise InvalidMarksError("Marks must be between 0 and 100")

        marks.append(mark)

except ValueError:
    print("Invalid input. Please enter numeric marks.")

except InvalidMarksError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)
else:
    student = Student(name, register_no, marks)
    print("\nStudent Details")
    print(student)
    print("Marks:", marks)
    print("Total:", student.calculate_total())
    print("Average:", student.calculate_average())
    print("Grade:", student.calculate_grade())

finally:
    print("Marks processing completed.")