# композиция
class Salary:
    def __init__(self, pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay * 12)


class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(self.pay)

    def annualSalary(self):
        return "Total: " + str(self.salary.getTotal() + self.bonus)


employee = Employee(100, 10)
print(employee.annualSalary())


# агрегация
class Salary2(object):
    def __init__(self, pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay * 12)


class Employee2(object):
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annualSalary(self):
        return "Total: " + str(self.pay.getTotal() + self.bonus)


employee2 = Employee2(100, 10)
print(employee.annualSalary())
