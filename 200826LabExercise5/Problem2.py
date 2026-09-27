class Employee:
    def __init__(self, EmployeeID, EmployeeName, BasicSalary):
        self.EmployeeID = EmployeeID
        self.EmployeeName = EmployeeName
        self.BasicSalary = BasicSalary

    def calculate_salary(self):
        pass

class PermanentEmployee(Employee):

    def __init__(self, EmployeeID, EmployeeName, BasicSalary):
        super().__init__(EmployeeID,EmployeeName, BasicSalary)

    def calculate_salary(self):
        return self.BasicSalary + (self.BasicSalary * 0.2)
            

class ContractEmployee(Employee):

    def __init__(self, EmployeeID, EmployeeName, BasicSalary):
        super().__init__(EmployeeID,EmployeeName, BasicSalary)

    def calculate_salary(self):
        return self.BasicSalary + (self.BasicSalary * 0.10)

class Intern(Employee):
        def __init__(self, EmployeeID, EmployeeName, BasicSalary):
                        super().__init__(EmployeeID,EmployeeName, BasicSalary)
       
        def calculate_salary(self):
             return self.BasicSalary

employee = []
employee1 = PermanentEmployee(1001,"Sathish", 5000)
employee2 = ContractEmployee(1002,"Renuka Devi", 40000)
employee3 = Intern(1004,"Suraj", 15000)

employee.append(employee1)
employee.append(employee2)
employee.append(employee3)
for em in employee:
    print("Employee ID:", em.EmployeeID)
    print("Employee Name:", em.EmployeeName)
    print("Basic Salary:", em.BasicSalary)
    print("Calculated Salary:", em.calculate_salary())
    print()
     
        
          