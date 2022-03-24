# Python Object-Oriented Programming

class Employee:  # class is like an object constructor, or a "blueprint" for creating objects.

    raise_amount = 1.15  # class attribute

    def __init__(self, first, last, pay,
                 was_born):  # The __init__() function/method is called automatically every time the
        # class is being used to create a new object.
        self.first = first  # attribute of class
        self.last = last  # attribute of class
        self.pay = pay  # attribute of class
        self.email = first.lower() + "." + last.lower() + "@ordubad.com"  # attribute of class
        self.was_born = was_born  # attribute of class

    def display_full_name(self):  # this is method/function ,by default self is always taken
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)


employee1 = Employee("Zeynal", "Hajili", 1000, "Ordubad")  # init method will run automatically to create employee1
# object ,employee1 will be passed as self to the function and arguments will be taken automatically
employee2 = Employee("Mamed", "Hajiyev", 1300, "Ordubad")

# print(employee2.first)
# print(employee1.email)
# print(employee1.display_full_name())
# print(Employee.display_full_name(employee2))

# print(employee1.pay,"<-- Old salary for Employee1")
# employee1.apply_raise()
# print(employee1.pay,"<-- New salary for Employee1")
# print(employee2.pay,"<-- Old salary for Employee2")
# employee2.apply_raise()
# print(employee2.pay,"<-- New salary for Employee2")
# print(employee2.__dict__)
# print(Employee.__dict__)

# Employee.raise_amount = 15
employee2.raise_amount = 19
employee1.raise_amount = 2
print(employee2.apply_raise())
print(employee2.pay)
print(employee1.apply_raise())
print(employee1.pay)
