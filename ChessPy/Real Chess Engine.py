for i in range(5) : print()

import pygame, sys#, numpy as nump
# from random import randint

ROW, COL = 12, 10
isGameOver = False
game_turn = True

# Colors
LIGHT_SQ = (220, 220, 230)
DARK_SQ = (127, 127, 255)
YELLOW = (255, 255, 127)
BLACK = (0, 0, 0)

# board_array = nump.full( (ROW, COL), -1 )
# board_array[nump.ix_(range(2, ROW - 2), range(1, COL - 1))] = 0

sqColor = lambda pos: (LIGHT_SQ, DARK_SQ)[(pos[0] + pos[1]) % 2]

class Coordinate:
	def __init__( self, tup ):
		self.update_coords(tup)

	def update_coords( self, tup ):
		# self.index = tup
		self.ind_r, self.ind_c = self.index = tup

	@property
	def cord_X( self ): return self.ind_c * SQUARE_SIZE + int((SQUARE_SIZE - PIECE_SIZE) / 2) + BORDER 
	@property
	def cord_Y( self ): return self.ind_r * SQUARE_SIZE + int((SQUARE_SIZE - PIECE_SIZE) / 2) + BORDER 
	@property
	def coords( self ): return (self.cord_X, self.cord_Y)
	
sqr_to = Coordinate( (0,0) )

class Board:
	
	position = ['~' * 10] * 2 + ['~rnbqkbnr~','~pppppppp~'] + ['~00000000~'] * 4 + ['~PPPPPPPP~','~RNBQKBNR~'] + ['~' * 10] * 2

	piece_obj = [[None] * 8 for _ in range(8)]

	@staticmethod
	def draw():
		for r in range(ROW - 4):
			for c in range(COL - 2):
				square = (r * SQUARE_SIZE + BORDER, c * SQUARE_SIZE + BORDER, SQUARE_SIZE, SQUARE_SIZE)
				pygame.draw.rect(screen, sqColor( (r, c) ), square)

	@staticmethod
	def set_position():
		for r in range(ROW - 4):
			for c in range(COL - 2):
				# board_array[r][c] = piece.islower() + 1
				piece = Board.position[r + 2][c + 1]
				
				if piece.isalpha():
					Board.piece_obj[r][c] = Piece.get_class( piece )
					Piece.draw ( Coordinate((r, c)), piece )
				# elif piece == '0':

		pygame.display.flip()

	@staticmethod
	def update_position( sqr, p ):
		Board.position[sqr.ind_r + 2] = Board.position[sqr.ind_r + 2][:sqr.ind_c + 1] + ('0' if p == ' ' else p) + Board.position[sqr.ind_r + 2][sqr.ind_c + 2:]



sqr_from = Coordinate((0,0))
is_selected = False

class Piece:
	def __init__( self, arg ):
		# super(Piece, self).__init__()
		self.arg = arg
	
	@staticmethod
	def get_class( piece_ch ):
		return { 'P': Pawn, 'N': Knight, 'B': Bishop, 'R': Rook, 'Q': Queen, 'K': King } [piece_ch.upper()]()

	@staticmethod
	def draw( ind, piece_sym ):
		label = chess_font.render(piece_sym, True, BLACK, sqColor( ind.index ))
		screen.blit( label, ind.coords )
		Board.update_position( ind, piece_sym )
		
	@staticmethod
	def move( indices ):
		sqr_to.update_coords( indices )

		get_piece_from = lambda idx: Board.position[idx.ind_r + 2][idx.ind_c + 1]
		global sqr_from, is_selected, game_turn

		print(sqr_to.index)
		piece = get_piece_from( sqr_to )

		if piece.isupper() if game_turn else piece.islower():	# First Click
			# if piece.upper() == 'B':
			# 	Bishop.show_path()

			Board.piece_obj[sqr_to.ind_r][sqr_to.ind_c].show_path()
			sqr_from.update_coords( sqr_to.index )
			is_selected = True

		elif is_selected:
			piece = get_piece_from( sqr_from )

			Piece.draw( sqr_from, ' ' )	# delete piece
			Piece.draw( sqr_to, piece )	# add to new index

			Board.piece_obj[sqr_to.ind_r][sqr_to.ind_c] = Board.piece_obj[sqr_from.ind_r][sqr_from.ind_c]
			Board.piece_obj[sqr_from.ind_r][sqr_from.ind_c] = None

			is_selected = False
			game_turn = not game_turn	# Switching Turn

class Pawn:
	@staticmethod
	def show_path():
		pass

class Knight:
	@staticmethod
	def show_path():
		pass

class Bishop:
	homes = []
	# @staticmethod
	def show_path(self):
		direction = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
		current_sqr = sqr_to.index #(sqr_to.ind_r + 2, sqr_to.ind_c + 1)
		
		print("Bishop at -", current_sqr)
		i = 1
		while any(direction):
			print(direction)
			for d, tup in enumerate(direction):
				if not not tup:
					current_sqr = (sqr_to.ind_r + tup[0] * i, sqr_to.ind_c + tup[1] * i)
					print(current_sqr)
					if Board.position[current_sqr[0] + 2][current_sqr[1] + 1] == '0':
						self.homes.append(current_sqr)
						Piece.draw(Coordinate(current_sqr), 'o')
					else:
						direction[d] = False
			i += 1
class Rook:
	@staticmethod
	def show_path():
		pass

class Queen:
	@staticmethod
	def show_path():
		pass

class King:
	@staticmethod
	def show_path():
		pass

SQUARE_SIZE = 60
BORDER = int( SQUARE_SIZE * 0.2 )
PIECE_SIZE = int( SQUARE_SIZE * 0.8 )

pygame.init()
pygame.display.set_caption('Real Chess Game')
# pygame.display.set_icon( pygame.image.load('Icon.jpg') )
chess_font = pygame.font.SysFont('Chess', PIECE_SIZE)

# pygame.mouse.set_visible(False)
# CURSOR = pygame.image.load('Cursors/Cool_Blue.png')

width = (COL - 2) * SQUARE_SIZE + BORDER * 2
height = (ROW - 4) * SQUARE_SIZE + BORDER * 2

screen = pygame.display.set_mode( (width, height) )

Board.draw()
Board.set_position()

while not isGameOver:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print(*Board.position[2:-2], sep='\n')
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if not (BORDER < event.pos[0] < width - BORDER and BORDER < event.pos[1] < height - BORDER):
				continue

			indices = tuple( int((n - BORDER) / SQUARE_SIZE) for n in event.pos )
			# print(indices, event.pos)

			Piece.move( indices[::-1] )

			pygame.display.update()

	# mouse_pos = pygame.mouse.get_pos()
	# screen.blit( CURSOR, (mouse_pos) )
	# pygame.display.update()



# screen.fill(pygame.Color('black'), (0, 0, SQUARE_SIZE, SQUARE_SIZE)) // to erase a piece