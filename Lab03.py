print('List Operations Program!')

print('Menu: \n1)Add a number to the list\n2)Remove a number from the list\n3)Insert a number at a specific postition\n4)Pop a number from the list\n5)Find the sum, average, and maximum of the list\n6)Search for a number in the list\n7)Remove all odd numbers from the list\n8)Exit\n')
menu = 0
num_list = []

while menu != 8:
    menu = int(input('Enter your choice: '))
    if (menu == 1):
        num = float(input('Add a number to the list: '))
        num_list.append(num)
        should_print = input('Would you like to print list? (yes/no): ')
        if (should_print == 'yes'):
            print(num_list)
        else: 
            print('Input yes.')
    elif (menu == 2):
        num = float(input('Remove a number from the list: '))
        num_list.remove(num)
        should_print = input('Would you like to print list? (yes/no): ')
        if (should_print == 'yes'):
            print(num_list)
        else: 
            print('Input yes.')
    elif (menu == 3):
        num = float(input('Insert a number: '))
        index = int(input('Enter the desired index position: '))
        num_list.insert(index, num)
        should_print = input('Would you like to print list? (yes/no): ')
        if (should_print == 'yes'):
            print(num_list)
        else: 
            print('Input yes.')
    elif (menu == 4):
        pop_index = int(input('Enter a index to remove: '))
        num_list.pop(pop_index)
        should_print = input('Would you like to print list? (yes/no): ')
        if (should_print == 'yes'):
            print(num_list)
        else:
            print('Input yes.')
    elif (menu == 5): 
        totalsum = sum(num_list)
        avg = totalsum / len(num_list)
        max_val = max(num_list)
        should_print = input('Would you like to print list? (yes/no): ')
        if (should_print == 'yes'):
            print(f'Sum: {totalsum}, Average: {avg:.2f}, Max: {max_val}')
        else: 
            print('Input yes or list may be empty')
    elif (menu == 6): 
        search = float(input('Number to search for: '))
        should_print = input('Would you like to print list? (yes/no): ')
        if search in num_list: 
            print(f'Number found at index: {num_list.index(search)}')
        else: 
            print('Number not found')
    elif (menu == 7):
        num_list = [num for num in num_list if num % 2 == 0]
        should_print = input('Would you like to print list? (yes/no): ')
        if (should_print == 'yes'):
            print('Odd numbers removed.')
            print(num_list)
        else: 
            print('Input yes')
    else: 
        print('Goodbye!')