a = 1 
b = 2
c = a + b

def test(_a, _b):
    c = _a + _b
    return c 

def test1(_a, _b):
    global c
    c= _a + _b

def test2(_a, _b):
    _a += 1
    _b -= 2
    c = _a + _b
    return _a, _b, c 

def test3(_a = 4, _b = 2):
    c = _a + _b
    return c 

def test4(_a, _b = 2):
    c = _a + _b 
    return c

def test5(_a, _c, _b = 2):
    c = _a + _b 
    return c

c = test4(1)
c = test3()
c = test3(1,2)


c = test(1,2)
test1(1,2)
a,b,c = test2(1,2)

class TestClass: 
    def __init__(self, _a = 2, _b =1):
        self.a = _a
        self.b = _b
        self.c = 0

    def test(self):
        self.c = self.a + self.b
        print("c value:", self.c)

testClass1 = TestClass(3,4)
testClass1.test()

testClass2 = TestClass(2,1)
# testClass2.a = 3
# testClass2.b = 2
testClass2.test()

l = [1,2,3]
print(l[0])
print(l[2])
print(len(l))
l1 = [1, False, 'hello', TestClass()]
print(l1)

testClass3 = TestClass(l[0], l[1])
testClass2.test()

l = [1,2,3]
l2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
l3 = [1,2,3]
l4 = [4,5,6]
l5 = [7,8,9]
l6 = [l3,l4,l5]

print(l2[1])
print(l2[1][2])
print(l6[1])
print(l6[1][2])

d = {"0": 4, "1": 5, "2": 6}
print(d["0"])

d = {"first": 4, "second": 5, "third": 6}
print(d["first"])