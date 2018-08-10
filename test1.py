import rubik as rubik

#print(rubik.Colors.ORANGE)
print("Before rotation\n")
face = rubik.Face(rubik.Positions.FRONT,rubik.Colors.ORANGE)
for piece in face.getPieces():
	print(piece.getPosition(), piece.getPieceCategory())

face.rotate(rubik.Movements.CLOCKWISE)

print("\nAfter CLOCKWISE rotation\n")
for piece in face.getPieces():
	print(piece.getPosition(), piece.getPieceCategory())


face.rotate(rubik.Movements.COUNTER_CLOCKWISE)

print("\nAfter COUNTER CLOCKWISE rotation\n")
for piece in face.getPieces():
	print(piece.getPosition(), piece.getPieceCategory())