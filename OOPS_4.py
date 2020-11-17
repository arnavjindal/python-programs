
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def num_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves


harry = Employee("Harry", 255, "Instructor")



harry.num_leaves(22)
print(Employee.no_of_leaves)
