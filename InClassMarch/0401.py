# a = [1,2,3,"shawn", True]
# print(a[0])
# print(a[2])
#------------------------------------------------------

# students = {}
# students ['Jose'] = {'Grade': 'A+', 'StudentID': 22321}
# students ['Shawn'] = {'Grade': 'F', 'StudentID': 00000}
# for key, value in students.items(): 
#     if key == 'Shawn':
#         print(value)

# print(students)
# print('Jose:')

# print(f' Grade: {students ["Jose"]["Grade"]}')

# print(f' ID: {students["Jose"]["StudentID"]}')

#------------------------------------------------------
# class Test: 
#     a = 1
# phones = {}
# phones ['Iphone'] = 1000
# phones ['Samsung'] = 800
# phones ['Galaxy'] = 600
# phones ['oneplus'] = Test
# print(phones)
# print(phones['Samsung'])

# price_list = [1000, 800, 600]
# phone_list = ['iphone', 'samsung', 'galaxy']
# print(phone_list[1], price_list[1])
# for values in price_list:
#     print(values)

#------------------------------------------------------
# cars = {}
# cars['Tacoma'] = 10000
# cars['Tundra']  = 12000
# cars['Venza'] = 11000
# print(cars)
# print('Tacoma', cars['Tacoma'])
# print('Tundra', cars['Tundra'])
# print('Venza', cars['Venza'])
# for key, values in cars.items():
#     print(key)
#     print(values)
# for key in cars.keys(): 
#     print(key)
# for values in cars.values(): 
#     print(values)

#------------------------------------------------------
# students = {}
# students ['Jose'] = {'Grade': 'A+', 'StudentID': 22321}
# students ['Shawn'] = {'Grade': 'F', 'StudentID': 00000}
# students ['aaa'] = {'Grade': 'A', 'StudentID': 22321}
# students ['bbb'] = {'Grade': 'F', 'StudentID': 00000}
# students ['ccc'] = {'Grade': 'A', 'StudentID': 22321}
# students ['ddd'] = {'Grade': 'F', 'StudentID': 00000}
# # for key, value in students.items(): 
# #     print(value)
# #     for info_key, info_value in value.items():
# #         if (info_value == 'F'):
# #             print(key)
# for key, value in students.items(): 
#     print(value)
#     if value['Grade'] == 'F':
#         print(key)
#         print(value['StudentID'])

#------------------------------------------------------
# students = {}
# students ['Jose'] = {'Grade': 'A+', 'StudentID': 22321}
# students ['Jose'] = {'Grade': 'C', 'StudentID': 23412}
# students ['Shawn'] = {'Grade': 'F', 'StudentID': 00000}
# students ['aaa'] = {'Grade': 'A', 'StudentID': 22321}
# students ['bbb'] = {'Grade': 'F', 'StudentID': 00000}
# students ['ccc'] = {'Grade': 'A', 'StudentID': 22321}
# students ['ddd'] = {'Grade': 'F', 'StudentID': 00000}
# students.update({'eee':{'Grade': 'F', 'StudentID': 00000}})
# students.pop('ddd')
# # print(students)
# # students.clear()
# print(students)
# # print(students.get('Shawn'))

#------------------------------------------------------
# class StudentInfo:
#     def __init__(self, _grade, _student_id):
#         self.grade = _grade
#         self.student_id = _student_id
#         pass
#     def display(self): 
#         print(self.student_id)
# student_class_dict = {}
# student_class_dict['Josh'] = StudentInfo('A+', 12345)
# student_class_dict['Shawn'] = StudentInfo('B', 90978)
# student_class_dict['aaa'] = StudentInfo('F', 23345)

# for key, value in student_class_dict.items():
#     if (value.grade == 'F'):
#         # print(value.display())
#         print(value.student_id)
#         print(key)

def test(): 
    return 2,3,False, [2,4]
a,b,c,d = test()
print(a)
print(b)
print(c)
print(d)