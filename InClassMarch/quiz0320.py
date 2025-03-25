# print('Menu:\n1)Add item to list\n2)Remove item from list\n3)Exit')
# user_choice = int(input('Input Menu Choice: '))
# my_list = []
# while user_choice != 3:
#     if user_choice == 1: 
#         add_string = input('String to add: ')
#         my_list.append(add_string)
#         print('Updated list:', my_list)
#         print('Menu:\n1)Add item to list\n2)Remove item from list\n3)Exit')
#         user_choice = int(input('Input Menu Choice: '))
#     elif user_choice == 2: 
#         remove_string = input('Type yes to remove last item from list: ')
#         if remove_string == 'yes':
#             my_list.pop()
#             print('Updated list:', my_list)
#             print('Menu:\n1)Add item to list\n2)Remove item from list\n3)Exit')
#             user_choice = int(input('Input Menu Choice: '))
#         else: 
#             print(my_list)
#             print('Menu:\n1)Add item to list\n2)Remove item from list\n3)Exit')
#             user_choice = int(input('Input Menu Choice: '))
# else: 
#         print('Final list:', my_list)
#         print('Goodbye')

#SOLUTIONS

# class MenuProgram:
#     def __init__(self):
#         self.item_list = []
#         self.menu_option = 0

#     def show_menu(self):
#         print('1. Add Item\n2. Remove Item')
#         self.menu_option = int(input('Enter option: '))
#     def display_output(self): 
#         print(self.item_list)
#     def run(self):
#         while self.menu_option !=3:
#             self.show_menu()
#             if self.menu_option == 1:
#                 item_name = input('Enter a item: ')
#                 self.item_list.append(item_name)
#                 self.display_output()
#             elif self.menu_option == 2: 
#                 self.item_list.pop()
#                 self.display_output()


# menu_program = MenuProgram()
# menu_program.run()

# counter = 10
# def count_down(count):
#     if count == -1:
#         print('Go!')
#     else:
#         print(count)
#         count_down(count-1)
# def count_up(count):
#     if count == 11:
#         print('Go!')
#     else: 
#         print(count)
#         count_up(count+1)
# count_down(counter)
# count_up(0)

def count(couter, down):
    if couter == 0: 
        down = False
        count(couter+1, down)
        print('Go!')
    elif couter == 10 and down == False:
        print('Done!')
    else: 
        if down==True:
            print(couter)
            count(couter-1, down)
        else:
            print(couter)
            count(couter+1, down)

count(10, True)