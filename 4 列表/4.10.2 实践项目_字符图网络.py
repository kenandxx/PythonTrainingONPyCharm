grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.',1,2,3],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]#9hang,各行6个
         
        
        
print(grid[0][0]+grid[0][1]+grid[0][2]+grid[0][3]+grid[0][4])
print(len(grid[0]))
print(len(grid[1]))
print()

i = 0
for i in range(6): #012345678
	for h in range(9): #012345
		print(grid[h][i], end = '')
	print()
	i += 1

"""
for (i, h) in zip(range(len(grid[0])), range(len(grid[1]))):
	print(str(i), str(h))
	# 这个方式只能打出最短的range
"""
#OUT 
"""
0 0
1 1
2 2
3 3
4 4
5 5
"""

