# line = ""
# for i in range(3):
#     for j in range(3):
#         line += str(i) + str(j)
#     print(line)
#     line = ""

# a_list = [0,1,2,3,4,5]
# print(a_list)
# a_list[2]=10
# print(a_list[2])

# a_list = [0,1,2,3,4,5]
# two_d_list = [[0,1,2,3,4],
#               [5,6,7,8,9],
#               [10,11,12,13]
#               ]
# print("two_d_list:", two_d_list)
# print("a_list:", a_list)
# print("a_list[1]:", a_list[1])
# print("two_d_list[1]:",two_d_list[1])
# print("two_d_list[1][1]:",two_d_list[1][1])

# two_d_list= []
# line = []
# for i in range(3):
#     for j in range(3):
#             line.append(str(i) + str(j) + " ")
#     two_d_list.append(line)
#     line = []
# print(two_d_list)

# print_line =" "
# for i in range(3):
#     for j in range(3):
#         print_line += two_d_list[i][j]
#     print(print_line)
#     print_line = " "
# print(print_line)


# two_d_list= []
# line = []
# for i in range(3):
#     for j in range(3):
#         if i == j: 
#             line.append('*')
#         else:
#             line.append(" ")
#     two_d_list.append(line)
#     line = []
# print(two_d_list)

# print_line =" "
# for i in range(3):
#     for j in range(3):
#         print_line += two_d_list[i][j]
#     print(print_line)
#     print_line = " "
# print(print_line)

import random 
num=random.randint(0,1)

visual_two_d_list= []
visual_line = []
for i in range(3):
    for j in range(3):
        visual_line.append('#')
        num=random.randint(0,1)
    visual_two_d_list(visual_line)
    visual_line = []
print(visual_two_d_list)

mine_two_d_list= []
mine_line = []
for i in range(3):
    for j in range(3):
        mine_line.append(num)
        num=random.randint(0,1)
    mine_two_d_list(mine_line)
    mine_line = []
    
print(mine_two_d_list)

input_x = int(input('input x position: '))
input_y = int(input('input y position: '))

if mine_two_d_list[input_x][input_y] == 1:
    visual_two_d_list[input_x][input_y] = 'X'
    print('You lose')
else:
    visual_two_d_list[input_x][input_y] = '_'
    print('keep going')
    
print(visual_two_d_list)

# print_line =[]
# for i in range(3):
#     for j in range(3):
#         print_line.append(mine_two_d_list[i][j])
        
    
#     print(print_line)
#     print_line = " "
# print(print_line)

