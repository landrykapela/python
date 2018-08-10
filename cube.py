import itertools
import operator as op

white = ["wc","wg","wb","wo","wr","wgo","wgr","wbo","wbr"]
orange = ["oc","wo","oy","og","ob","wbo","wgo","oby","ogy"]
yellow = ["yc","yg","yb","oy","yr","ogy","ygr","oby","ybr"]
red = ["rc","wr","ry","rg","rb","wbr","wgr","ybr","ygr"]
blue = ["bc","by","wb","ob","rb","oby","ybr","wbo","wbr"]
green = ["gc","wg","yg","rg","og","wgr","ygr","ogy","wgo"]

colors = ["w","b","y","g","r","o"]
opposite_colors = [("w","y"),("b","g"),("o","r")]

edge_pieces = []
cs = len(colors)
for i in range(cs):
	item = []
	k = i + 1
	if k < cs:
		item = tuple([colors[i],colors[k]])
	else:
		item = tuple([colors[i],colors[0]])
	colors = colors[i:cs]
	edge_pieces.append(item)

print(edge_pieces, len(edge_pieces))
#white_orange = list(itertools.ifilter(lambda x: x in white and x in orange,itertools.chain(white,orange)))

#print(white_orange, len(white_orange))