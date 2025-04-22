# a = 1 
# b = 2
# c = a + b

# def test(_a, _b):
#     c = _a + _b
#     return c 

# def test1(_a, _b):
#     global c
#     c= _a + _b

# def test2(_a, _b):
#     _a += 1
#     _b -= 2
#     c = _a + _b
#     return _a, _b, c 

# def test3(_a = 4, _b = 2):
#     c = _a + _b
#     return c 

# def test4(_a, _b = 2):
#     c = _a + _b 
#     return c

# def test5(_a, _c, _b = 2):
#     c = _a + _b 
#     return c

# c = test4(1)
# c = test3()
# c = test3(1,2)


# c = test(1,2)
# test1(1,2)
# a,b,c = test2(1,2)

# class TestClass: 
#     def __init__(self, _a = 2, _b =1):
#         self.a = _a
#         self.b = _b
#         self.c = 0

#     def test(self):
#         self.c = self.a + self.b
#         print("c value:", self.c)

# testClass1 = TestClass(3,4)
# testClass1.test()

# testClass2 = TestClass(2,1)
# # testClass2.a = 3
# # testClass2.b = 2
# testClass2.test()

# l = [1,2,3]
# print(l[0])
# print(l[2])
# print(len(l))
# l1 = [1, False, 'hello', TestClass()]
# print(l1)

# testClass3 = TestClass(l[0], l[1])
# testClass2.test()

# l = [1,2,3]
# l2 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# l3 = [1,2,3]
# l4 = [4,5,6]
# l5 = [7,8,9]
# l6 = [l3,l4,l5] # key for list is index

# print(l2[1])
# print(l2[1][2])
# print(l6[1])
# print(l6[1][2])

# d = {"0": 4, "1": 5, "2": 6} # key for dictionary is the key you defined ie: "first"
# print(d["0"])

# d = {"first": 4, "second": 5, "third": 6}
# print(d["first"])

l2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in range(len(l2)):
    print(l2[i])
    for j in range(len(l2[i])):
        print(l2[i][j])
        

l = [1,2,3]
for i in l: 
    print(i)

d = {"first": 4, "second": 5, "third": 6}
for i in d: 
    print(i)
for key, value in d.items(): 
    print(key, value)

for value in d.values(): 
    print(value)

class Student: 
    def __init__(self, name, age):
        self.n = name 
        self.a = age

    def drinking(self):
        if self.a > 21:
            print('Cannot drink, under 21. Age:', self.a)


student3 = Student('K', 21)
student3.drinking()
