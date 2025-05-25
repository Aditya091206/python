print("name:aditya.M,USN:1AY24AI004,sec:'M")
grid=[
    ['.','.','.','.','.','.'],
    ['.','0','0','.','.','.'],
    ['0','0','0','0','.','.'],
    ['.','0','0','0','0','0'],
    ['0','0','0','0','0','.'],
    ['0','0','0','0','.','.'],
    ['.','0','0','.','.','.'],
    ['.','.','.','.','.','.',]
]
for col in range(len(grid[0])):
# loop through colums
    for row in range(len(grid)):
# loop through rows
        print(grid[row][col],end=' ')#print column-wise
    print()
# new line after each column