from sudoku import *
import time

#Solver for the sudoku puzzle
def solve(sudoku):
	numbers = sudoku.numbers
	

def main():
	sudoku = Sudoku('layout.txt')
	print 'Puzzle:'
	print sudoku
	print 'Answer:'
	start = time.time()
	print solve(sudoku)
	end = time.time()
	print 'Time Elapsed: ' + str(end - start) + 's'

if __name__ == "__main__":main()