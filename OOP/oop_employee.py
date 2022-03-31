# Python Object-Oriented Programming
# YouTube Playlist
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&ab_channel=CoreySchafer
import csv


class Employee:  # class is like an object constructor, or a "blueprint" for creating objects.

    number_of_employees = 0  # class attribute aka class variable
    raise_amount = 1.2  # class attribute aka class variable

    def __init__(self, first, last, pay,
                 was_born):  # The __init__() function/method is called automatically every time the
        # class is being used to create a new object.
        self.first = first  # attribute of class
        self.last = last  # attribute of class
        self.pay = pay  # attribute of class
        self.email = first.lower() + "." + last.lower() + "@ordubad.com"  # attribute of class
        self.was_born = was_born  # attribute of class
        Employee.number_of_employees = Employee.number_of_employees + 1

    def write_email_addresses_to_csv(self):
        with open("email_addresses.csv", "a", newline="\n") as write_to_csv:
            writer = csv.writer(write_to_csv)
            writer.writerow([ self.email ])

    def display_full_name(self):  # this is regular method/function ,by default self is always taken as first argument
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        # self.pay = int(self.pay * self.raise_amount)
        self.pay = int(self.pay * self.raise_amount)

    @classmethod  # class method ,in class method class is taken as argument ,not the instance ( self)
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def parse_string_create_users(cls, string_name_to_input):
        first, last, pay, born = string_name_to_input.split("-")
        return cls(first, last, pay, born)


class Developers(Employee):  # child class ,parent class is Employee
    raise_amount = 1.7

    def __init__(self, first, last, pay, was_born, programming_language):
        super().__init__(first, last, pay, was_born)
        self.programming_language = programming_language


class Manager(Employee):  # child class ,parent class is Employee
    def __init__(self, first, last, pay, was_born, employees=None):
        super().__init__(first, last, pay, was_born)
        if employees is None:
            self.employees = []
            print("{} does not have any employee :)  ".format(self.first))
        else:
            # print("{} has following employee list  ".format(self.first))
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employee(self):
        for emp in self.employees:
            print(" ---> ", emp.display_full_name())


# print(Employee.number_of_employees)

employee1 = Employee("Zeynal", "Hajili", 1000, "Ordubad")  # init method will run automatically to create employee1
# object ,employee1 will be passed as self to the function and arguments will be taken automatically
employee2 = Employee("Mamed", "Hajiyev", 2000, "Ordubad")
employee3 = Employee("Haji", "Hajiyev", 0, "Julfa")
employee4 = Employee("Huseyn", "Hajiyev", 999, "Baku")
employee5 = Employee("Bagi", "Mammadov", 0, "Baku")
dev1= Developers("John", "Kennedy", 4000, "Orlando", "GoLang")
dev2 = Developers("Bark", "Chris", 5000, "California", "Ruby")
dev3 = Developers("Toghrul", "Azizli", 14000, "Shaki", "Java")
dev4 = Developers("Chris", "Cosh", 11000, "California", "C++")
emp6_string = "Mahmud-Mahmudov-899-Cuba"
emp7_string = "Kubra-Mahmudova-99-Ganja"
Employee.write_email_addresses_to_csv(employee5)
Employee.write_email_addresses_to_csv(employee4)
Employee.write_email_addresses_to_csv(employee3)
Employee.write_email_addresses_to_csv(employee2)
Employee.write_email_addresses_to_csv(employee1)

# print(Employee.parse_string_create_users(emp7_string))
employee7 = Employee.parse_string_create_users(emp7_string)
employee6 = Employee.parse_string_create_users(emp6_string)
# print(employee7.email)
# print(employee6.first)
# print(employee7.pay)
# print(employee2_developers.pay)
# print(employee2_developers.apply_raise())
# print(employee2_developers.first)
# print(employee2_developers.pay)
# print(employee2_developers.programming_language)
# print(employee1_developers.programming_language)
# print(employee4_developers.programming_language)
# print(employee3_developers.programming_language)
manager1 = Manager("Damian", "Wrobel", 20000, "Krakow", [ dev1 ])
manager2 = Manager("Diana", "Nowak", 21000, "Krakow")
manager1.add_employee(dev3)
manager1.add_employee(dev2)
manager1.print_employee()
