# Python Object-Oriented Programming
# YouTube Playlist
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&ab_channel=CoreySchafer


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

    def write_email_addresses(self):
        with open("email_addresses.txt","w") as write_to_txt:
            write_to_txt.write(self.email)

    def display_full_name(self):  # this is regular method/function ,by default self is always taken as first argument
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        # self.pay = int(self.pay * self.raise_amount)
        self.pay = int(self.pay * Employee.raise_amount)
    #
    # @classmethod  # class method
    # def set_raise_amount(cls, amount):
    #     cls.raise_amount = amount
    # # @classmethod

# print(Employee.number_of_employees)
#
employee1 = Employee("Zeynal", "Hajili", 1000, "Ordubad")  # init method will run automatically to create employee1
# object ,employee1 will be passed as self to the function and arguments will be taken automatically
employee2 = Employee("Mamed", "Hajiyev", 2000, "Ordubad")
employee3 = Employee("Haji", "Hajiyev", 0, "Julfa")
employee4 = Employee("Huseyn", "Hajiyev", 999, "Baku")
employee5 = Employee("Bagi", "Mammadov", 0, "Baku")
# employee5.raise_amount = 1.3
# employee5.set_raise_amount(11)
# # employee5.was_born = "Nakchivan"  # instance variable
# # employee4.pay = 350  # instance variable
# # print(employee4.__dict__)
# # print(Employee.number_of_employees)
# # print(employee5.was_born)
# Employee.set_raise_amount(10)
# print(Employee.raise_amount)
# print(employee5.raise_amount)
# print(employee4.raise_amount)
#
# emp6_string = "Mahmud-Mahmudov-899-Cuba"
# emp7_string = "Kubra-Mahmudova-99-Ganja"
# name, last_name, pay,place = emp6_string.split("-")
# employee6 = Employee(name,last_name,pay,place)

Employee.write_email_addresses(employee5)
