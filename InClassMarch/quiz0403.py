# grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# total = 0 

# def sum_region(grid, row):
#     global total
    
#     print(grid[row])
#     for j in grid[row]:
#         print(j)
#         total += j

#     if(row < 2):
#         sum_region(grid, row + 1)

# sum_region(grid, 0)  # Output: 45

# print(total)

#______________________________________________________________________ 

# def sum_region(grid, row):
#     global total
#     print(grid)
#     for key, value in grid.items():
#         print(key)
#         print(value)
#         for key_inner, value_inner in value.items(): 
#             print(key_inner)
#             print(value_inner)
#             total += value_inner


# grid_dict = {}
# grid_dict.update ({'0':{'0' : 1, '1': 2, '2': 3}})
# grid_dict.update ({'1':{'0' : 4, '1': 5, '2': 6}})
# grid_dict.update ({'2':{'0' : 7, '1': 8, '2': 9}})

# sum_region(grid_dict, 0)
# print(total)

#______________________________________________________________________

# grid_dict = {}
# grid_dict.update ({'0':{'0' : 0, '1': 0, '2': 0}})
# grid_dict.update ({'1':{'0' : 0, '1': 0, '2': 0}})
# grid_dict.update ({'2':{'0' : 0, '1': 0, '2': 0}})

# def modify_dict(grid_dict):
#     for key, value in grid_dict.items():
#         # print(key)
#         # print(value)
#         for key_inner, value_inner in value.items(): 
#             # print(key_inner)
#             # print(value_inner)
#             grid_dict[key][key_inner] = int(input('Enter a number at ' +key + " " + key_inner+ ": "))
#     print(grid_dict)

# modify_dict(grid_dict)

#______________________________________________________________________

class FancyDict: 
    def __init__(self):
        self.grid_dict = {}
        self.key_inner = 0
        self.key = 0 
        self.total = 0 
        pass

    def getUserInput(self): 
        for i in range(3):
            # self.grid_dict[i] = int(input('Enter a number at ' +str(i)+ ": "))
            self.grid_dict[i] = {}
            for j in range(3):
                self.grid_dict[i][j] = int(input('Enter a number at ' +str(i)+ ": "))

        print(self.grid_dict)
        

    def display(self):
        for key, value in self.grid_dict.items(): 
            for key_inner, value_inner in value.items():
                self.total += value_inner


fancyDict = FancyDict()
fancyDict.getUserInput()
fancyDict.display()