class Colors:
	WHITE = 0
	YELLOW = 1
	BLUE = 2
	GREEN = 3
	RED = 4
	ORANGE = 5


class Movements:
	CLOCKWISE = 0
	COUNTER_CLOCKWISE = 1

class Positions:
	DEFAULT = -1
	CENTER = 0
	EDGE = 1
	CORNER = 2

	TOP = 100
	FRONT = 101
	BACK = 102
	BOTTOM = 103
	LEFT = 104
	RIGHT = 105
	FACE_POSITIONS = [TOP,BOTTOM,FRONT,BACK,LEFT,RIGHT]

#public class for a puzzle piece
class Piece:
	#attributes
	position = []
	color = []
	category = -1;

	#public constructor
	def __init__(self,position, color):
		self.position = position
		self.color = color
		if(len(color) ==1):
			self.category = Positions.CENTER
		
		elif len(color) ==2:
			self.category = Positions.EDGE
		else:
			self.category = Positions.CORNER

	def setPosition(self,position):
		self.position = position
	

	def setColor(color):
		self.color = color
	

	#return array of x,y,z coordinates
	def getPosition(self):
		return self.position
	
	#return x cordinate
	def getXPosition(self):
		return self.position[0]
	
	#get y coordinate
	def getYPosition(self):
		return self.position[1]
	
	#get z coordinate
	def getZPosition(self):
		return self.position[2]
	
	#check if piece is a center piece
	def isCenterPiece(self):
		if self.category == Positions.CENTER:
			return True
		
		else:
			return False
	
	#check if piece is a edge piece
	def isEdgePiece(self):
		if self.category == Positions.EDGE:
			return True
		
		else:
			return False
	
	#check if piece is a corner piece
	def isCornerPiece(self):
		if self.category == Positions.CORNER:
			return True
		
		else:
			return False

	def getPieceCategory(self):
		cat_names = ["Center Piece","Edge Piece","Corner Piece"]
		
		return cat_names[self.category]


class Face:
	
	"""class Face defines the faces of a rubik's cube and their attributes"""

	Positions.FACE_POSITIONS = [Positions.TOP,Positions.BOTTOM,Positions.FRONT,Positions.BACK,Positions.LEFT,Positions.RIGHT]
	position = Positions.DEFAULT
	#color
	pieces = []

	#public constructor
	def __init__(self,position, color):
		try:
			self.position = Positions.FACE_POSITIONS[Positions.FACE_POSITIONS.index(position)]
			self.color = color
			color_left = color
			color_right= color
			color_top = Colors.WHITE
			color_bottom= Colors.YELLOW

			if color == Colors.ORANGE:
				color_left = Colors.BLUE
				color_right= Colors.GREEN
			elif color == Colors.GREEN:
				color_left = Colors.ORANGE
				color_right= Colors.RED
			elif color == Colors.RED:
				color_left = Colors.GREEN
				color_right= Colors.BLUE
			elif color == Colors.BLUE:
				color_left = Colors.RED
				color_right= Colors.ORANGE

			if position == Positions.FRONT:
				x = 0
				y = 0
				z = 1
				for i in range(9):
					if i < 3:
						y = 1
						if i == 0:
							x = -1
							piece_colors = [color_top,color,color_left]
						elif i == 1:
							x = 0
							piece_colors = [color_top,color]
						else:
							x = 1
							piece_colors = [color_top,color,color_right]
					elif 3 <= i < 6:
						y = 0
						if i == 3:
							x = -1
							piece_colors = [color_left,color]
						elif i == 4:
							x = 0
							piece_colors = [color]
						else:
							x = 1
							piece_colors = [color,color_right]
					else:
						y = -1
						if i == 6:
							x = -1
							piece_colors = [color_bottom,color,color_left]
						elif i == 7:
							x = 0
							piece_colors = [color_top,color]
						else:
							x = 1
							piece_colors = [color_top,color,color_right]		
					piece_postition = [x,y,z]
					piece = Piece(piece_postition,piece_colors)
					self.pieces.append(piece)
		except IndexError:
			print("Invalid Face Position")
		
		
		#public methods (setters and getters)
	def rotate(self,movement):
		if(movement == Movements.CLOCKWISE):
			for piece in self.pieces:
				if self.position == Positions.FRONT:
					x = 1*piece.getYPosition()
					y = -1*piece.getXPosition()
					pos = [x,y,piece.getZPosition()]
					piece.setPosition(pos)
		else:
			for piece in self.pieces:
				if self.position == Positions.FRONT:
					x = -1*piece.getYPosition()
					y = 1*piece.getXPosition()
					pos = [x,y,piece.getZPosition()]
					piece.setPosition(pos)
			
		
	def setColor(color):
		self.color = color
	

	#return array of x,y,z coordinates
	def getPosition(self):
		return self.position
	
	#return x cordinate
	def getXPosition(self):
		return self.position[0]
	
	#get y coordinate
	def getYPosition(self):
		return self.position[1]
	
	#get z coordinate
	def getZPosition(self):
		return self.position[2]
	
	def getPieces(self):
		return self.pieces


