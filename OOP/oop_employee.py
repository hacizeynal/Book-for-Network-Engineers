# Python Object-Oriented Programming

class Employee:  # class is like an object constructor, or a "blueprint" for creating objects.
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


employee1 = Employee("Zeynal", "Hajili", 8000, "Ordubad")  # init method will run automatically to create employee1
# object ,employee1 will be passed as self to the function and arguments will be taken automatically
employee2 = Employee("Mamed", "Hajiyev", 9000, "Ordubad")

print(employee2.first)
print(employee1.email)
print(employee1.display_full_name())