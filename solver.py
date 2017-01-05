from sudoku import *
from random import *
import sys
import time

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#Solver for the sudoku puzzle (medium fast)
def solveSimple(sudoku, index, positions):
	#Recursive Solver
	if sudoku.haveSolved():
		return sudoku

	row, col, numbers = positions[index]
	numbers = numbers[:]

	#Finds a valid number to put in that position
	num = 9
	for i in range(len(numbers)):
		if sudoku.validMove(row, col, numbers[i]):
			num = i

	#Adds number to position then move onto the next empty position
	if num < len(numbers):
		if sudoku.validMove(row, col, numbers[num]):
			sudoku.grid[row][col] = numbers[num]
			if index < len(positions) - 1:
				positions[index + 1][2] = number[:]
				return solveSimple(sudoku, index + 1, positions)
			return solveSimple(sudoku, index, positions)
	#Error a number was wrong so backtracking
	else:
		#Goes to previous empty position and remove the number that was used
		row, col, numbers = positions[index - 1]
		numbers.remove(sudoku.grid[row][col])
		sudoku.grid[row][col] = '_'
		return solveSimple(sudoku, index - 1, positions)

def main():
	sys.setrecursionlimit(22787)
	sudoku = Sudoku('layout.txt')
	print 'Puzzle:'
	print sudoku
	print 'Answer:'
	start = time.time()
	print solveSimple(sudoku, 0, sudoku.findEmpty())
	end = time.time()
	print 'Time Elapsed: ' + str(end - start) + 's'

if __name__ == "__main__":main()