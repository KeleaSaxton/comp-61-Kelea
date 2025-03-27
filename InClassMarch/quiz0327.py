# class Person:
#     def __init__(self):
#         self.money = int(input('Enter money: '))
#         self.firstname = str(input('Enter first name: '))
#         self.lastname = str(input('Enter last name: '))
#         self.dailysalary = int(input('Enter daily salary: '))
#         self.days = int(input('Enter days worked: '))
#         self.salary = 0
#     def work(self):
#         self.salary = self.days * self.dailysalary
#         self.money = self.salary + self.money
#         print(f'Salary: {self.salary}\nMoney: {self.money}')

# p1= Person()
# p1.work()

# p2 = Person()
# p2.work()

# class Person:
#     def __init__(self, _firstname, _lastname, _daily):
#         self.money = 0
#         self.firstname = _firstname
#         self.lastname = _lastname
#         self.dailysalary = _daily

#     def work(self, _days):
#         salary = _days * self.dailysalary
#         self.money = salary + self.money


# Shawn = Person('shawn', 'lin', 10)
# ben = Person('ben', 'ben', 20)

# Shawn.work(30)
# ben.work(15)

# if (Shawn.money > ben.money):
#     print('Shawn has more money')
# else:
#     print('Ben has more money')

# class Person:
#     pass
# e_list = ['a', True, 1, Person()]
# a_list = [1,2,3]
# b_list = [4,5,6]
# c_list = [a_list, b_list]  #2d list
# d_list = [[1,2,3],
#           [4,5,6]]
# print(c_list[0]) #1d list
# print(c_list[0][1]) # get #2 for from alist

import random
class Person:
    def __init__(self, _firstname, _lastname, _daily):
        self.money = 0
        self.firstname = _firstname
        self.lastname = _lastname
        self.dailysalary = _daily
        self.salary_list = []

    def work(self, _days):
        salary = _days * self.dailysalary
        self.money = salary + self.money

    def work_a_month(self):
        salary = 30 * self.dailysalary * random.random()
        self.salary_list.append(salary)

namelist = []
Shawn = Person('shawn', 'lin', 10)
namelist.append(Shawn)
ben = Person('ben', 'ben', 20)
namelist.append(ben)
k = Person('k', 's', 18)
namelist.append(k)
p = Person('p', 's', 19)
namelist.append(p)

Shawn.work(30)
ben.work(15)
k.work(28)
p.work(25)

for i in range(12):
    Shawn.work_a_month()

rich_person = None
most_monthly_salary = 0
month = 0
for i in range(len(namelist)):
    for j in range(len(namelist[i].salary_list)):
        if namelist[i].salary_list[j] >most_monthly_salary:
            rich_person = namelist[i]
            most_monthly_salary = namelist[i].salary_list[j]
            month = j + 1

print(rich_person.firstname, most_monthly_salary)



# namelist = [Shawn, ben, k, p]
# rich_person = None
# most_daily_salary = 0
# for name in namelist: 
#     if(name.dailysalary > most_daily_salary):
#         rich_person = name
#         most_daily_salary = rich_person.dailysalary

# for i in range(len(namelist)):
#     if namelist[i].dailysalary >most_daily_salary:
#         rich_person = namelist[i]
#         most_daily_salary = rich_person.dailysalary


# print(rich_person.firstname, rich_person.lastname)

# if (Shawn.money > ben.money):
#     print('Shawn has more money')
# else:
#     print('Ben has more money')