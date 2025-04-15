# x = -1
# while (x != 0):
#     try: 
#         x = 3
#         y = 3+1
#         x = int(input('Please enter a number: '))
#     except: 
#         print('Something went wrong')
#     finally: 
#         x = 2

#     if (x == 1):
#         print('Hello')
#     elif (x == 2):
#         print('Bye')

# print('Finish')

#-----------------------------------------------------------------------
# a = -1 
# b = ""
# while True:
#     try: 
#         a = int(input('Enter a input: '))
#     except: 
#         print('Something went wrong')
#     else: 
#         print('you entered', a)
#     finally: 
#         print("i am gonna run anyway")
    
#     b = input('Enter a string: ')
#     if a ==1: 
#         print('hello')
#     if b == 'lol':
#         print('hellohello')
#     try: 
#         if a + b == 3: 
#             print('hihihi')
#     except: 
#         print('Looks like the type may mismatch')
        
#-----------------------------------------------------------------------

# a = -1 
# b = "abc"
# c = 0
# try: 
#     a = int(input('enter a int number: '))
#     c = a + b
# except TypeError as e: 
#     print(e)
#     c = 3
# except Exception as e: 
#     print(e)
#     print('Entered a string instead of int')
# finally: 
#     print('This gonna run anyway')
# if(c == 3):
#     print('Hello')
# print('a:', a)

#-----------------------------------------------------
b = 2
def test_input():
    global b 
    try: 
        _a = int(input('enter a int number: '))
        return _a
    except Exception as e: 
        print(e)
    else: 
        _a = 2
    finally: 
        b = 3
        print('hello')
        _a = 3
        return _a

a = 3
a = test_input()
print(a+b)