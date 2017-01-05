#Sudoku puzzle
class Sudoku:
	grid = []

	number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

	#Initialize Grid 
	def __init__(self, files):
		#Read puzzle layout from file
		layout = open(files, 'r')
		self.grid = []
		for line in layout:
			line = line.split()
			row = []
			for num in line:
				row.append(num)
			self.grid.append(row)

	#Create string format of grid
	def __str__(self):
		output = ''
		for i in range(len(self.grid)):
			for j in range(len(self.grid)):
				output += self.grid[i][j] + ' '
			output += '\n'
		return output

	#Create list of empty spots
	def findEmpty(self):
		empty = []
		for i in range(len(self.grid)):
			for j in range(len(self.grid)):
				if self.grid[i][j] == '_':
					empty.append([i, j, self.number[:]])
		return empty

	#Checks if number is in horizontal
	def checkHoriz(self, row, num):
		return num in self.grid[row]

	#Checks if number is in verical
	def checkVert(self, col, num):
		for i in range(len(self.grid)):
			if num == self.grid[i][col]:
				return True
		return False

	#Finds the top left corner of 3x3 grid
	def calculateGrid(self, row, col):
		start_x = row/3
		start_y = col/3
		return start_x * 3, start_y * 3

	#Checks if number is in 3x3 grid
	def checkGrid(self, row, col, num):
		start_x, start_y = self.calculateGrid(row, col)
		for i in range(3):
			for j in range(3):
				if num == self.grid[start_x + i][start_y + j]:
					return True
	 	return False

	#Checks if num can be placed at that position
	def validMove(self, row, col, num):
	 	return not (self.checkHoriz(row, num) or self.checkVert(col, num) or self.checkGrid(row, col, num))

	#Checks if sudoku has been solved
	def haveSolved(self):
	 	for i in range(len(self.grid)):
			for j in range(len(self.grid)):
				if self.grid[i][j] == '_':
					return False
		return True