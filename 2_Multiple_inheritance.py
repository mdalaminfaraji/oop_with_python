class Company:
    def __init__(self, cname, location) -> None:
        self.cname=cname
        self.location=location
    def company_details(self):
        print(f'company Name  {self.cname} Location {self.location}')

class Person:
    def __init__(self, pname, age) -> None:
        self.pname=pname
        self.age=age
    def person_details(self):
        print(f'Name= {self.pname} age = {self.age}')

class Employee(Company, Person):
    def __init__(self, emp_name, emp_ege, cmp_name, cmp_location) -> None:
        Person.__init__(self, emp_name, emp_ege)
        Company.__init__(self, cmp_name, cmp_location)

obj_emp=Employee("alamin",23, "google", "usa")
obj_emp.person_details()
obj_emp.company_details()        

        