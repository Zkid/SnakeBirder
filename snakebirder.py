import random

# a rectangular game board, containing the snakebird, obstacles, food, and the end portal.
class Board():

	def __init__(self, board, snakebird=None):
		self.board = board
		self.width = len(board[0])
		self.length = len(board)
		self.snakebird = snakebird
		self.MOVES = {
			'down': (1, 0),
			'up'  : (-1, 0),
			'left': (0, -1),
			'right':(0, 1)
		}

	def update_location(self, coord, new_value):
		self.board[coord[0]][coord[1]] = new_value

	def get_location_value(self, coord):
		return self.board[coord[0]][coord[1]]

	def is_on_board(self, new_coord, width, length):
		pass

	def count_occurences(self, value):
		occurences = 0
		for i in range(self.length):
			occurences += self.board[i].count(value)
		return occurences

	def is_legal_location(self, new_coord, width, length):
		return (0 <= new_coord[0] < self.length and 0 <= new_coord[1] < self.width and self.board[new_coord[0]][new_coord[1]] in (' ', 'F', 'P'))

	def get_value(self, coord):
		if not is_legal_location(coord, self.width, self.length):
			return -1
		return self.board[coord[0]][coord[1]]

	def add_snakebird(self, snakebird):
		self.snakebird = snakebird
		for coord in self.snakebird.coords:
			if not self.is_legal_location(coord, self.width, self.length):
				print "Not legal location: " + str(coord)
				return False
		for coord in self.snakebird.coords:
			self.update_location(coord, 'S')
		head = self.snakebird.head
		self.update_location(coord, 'H')
		return True

	def make_snakebird_move(self, move):
		direction = self.MOVES[move]
		new_head_coord = (self.snakebird.head[0] + direction[0], 
			self.snakebird.head[1] + direction[1])
		
		if self.is_legal_location(new_head_coord, self.width, 
			self.length):
			ate = (self.get_location_value(new_head_coord) == 'F') # was food there
			(new_coords, old_coords) = self.snakebird.move(direction, ate)
			if not ate:
				self.update_location(old_coords[0], ' ') # won't work if ate 
			new_head = new_coords[-1]
			if len(new_coords) > 1:
				self.update_location(new_coords[-2], 'S')
			self.update_location(new_coords[-1], 'H')
		else:
			print "Illegal move attempted to " + str(new_head_coord)

	def __str__(self):
		boardprint = "Width: " + str(self.width)+ " Height: " + str(self.length) + "\n"
		for i in range(self.length):
			boardprint += (str(self.board[i]))
			boardprint += "\n"
		return boardprint 

class SnakeBird():

	def __init__(self, coords):
		self.coords = coords
		self.head = coords[-1] # tail to head list
		self.size = len(coords)

	def move(self, direction, ate):
		old_coords = self.coords
		new_coords = self.coords[1:]
		last_coord = (self.head[0] + direction[0], self.head[1] +
		    direction[1])
		new_coords.append(last_coord)
		if ate:
			new_coords.insert(0, self.coords[0])
		self.coords = new_coords
		self.head = self.coords[-1]
		print "Old snakebird coordinates: " + str(old_coords)
		print "Movement: " + str(direction)
		print "New snakebird coordinates: " + str(new_coords) + "\n"
		return (new_coords, old_coords)

	def __str__(self):
		return str(self.coords) + "\n"

def generate_random_board(length, width, density):
	board_template = [[' '] * width for i in range(length)]
	for i in range(length):
		for j in range(width):
			if random.random() < density:
				board_template[i][j] = 'T'

	return board_template

def play_snakebird(board, snakebird):
	board.add_snakebird(snakebird)
	print board
	while True:
		snakebird_move = raw_input("What is your next move? ")
		print snakebird_move
		if snakebird_move == 'finish':
			break
		board.make_snakebird_move(snakebird_move)
		print board


BOARD_TEMPLATE_1 = [[' ', 'T', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', 'T']]

BOARD_TEMPLATE_2 = [[' ', 'P', ' ', ' '],
                    [' ', ' ', 'T', ' '],
                    [' ', 'F', ' ', ' ']]

BOARD_TEMPLATE_3 = generate_random_board(10, 10, .2)

snakebird = SnakeBird([(1, 1), (1, 0)])
snakebird_board = Board(BOARD_TEMPLATE_3)
'''print "Add snakebird: " + str(snakebird_board.add_snakebird(snakebird))
print(snakebird_board)

snakebird_board.make_snakebird_move((1, 0))
print (snakebird_board)
snakebird_board.make_snakebird_move((0, 1))
print (snakebird_board)
snakebird_board.make_snakebird_move((0, -1))
print (snakebird_board)
snakebird_board.make_snakebird_move((0, 1))
print (snakebird_board)'''

play_snakebird(snakebird_board, snakebird)



