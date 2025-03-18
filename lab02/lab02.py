balance = float(1000.00)

print('Welcome to Simple ATM Simulator!')
print(f'Your current balance is: ${balance}\n')
print('Menu: \n1)Check Balance\n2)Deposit Money\n3)Withdraw Money\n4)Exit\n')
menu = 0
while menu != 4:
    menu = int(input('Enter Menu Choice: '))
    if (menu == 1):
        print(f'Your current balance is: ${balance:.2f}')
    elif (menu==2):
        deposit = float(input('Enter the amount to deposit: $'))
        balance = deposit + balance
        print(f'Deposit successful! New balance: ${balance:.2f}')
    elif (menu == 3):
        withdraw = float(input('Enter the amount to withdraw: $'))
        if withdraw > balance: 
            print(f'Insufficient Funds. Current balance: ${balance}')
        else: 
            balance = balance - withdraw
            print(f'New balance: ${balance:.2f}')
    elif (menu == 4):
        print('Thank you for using the ATM. Goodbye!')
    else: 
        print('Invalid menu choice. Enter 1 - 4.')
