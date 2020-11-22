liste = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
ordonare = liste.copy()
ordonare.sort()
print("Lista ordonata crescator este: ", ordonare)

ordonare.reverse()
print("Lista ordonata descrescator este: ", ordonare)

ordonare.sort()
print("Elementele pare din lista sunt: ", ordonare[1::2])
print("Elementele impare din lista sunt: ", ordonare[0::2])
print("Elementele multiplu de 3 din lista sunt: ", ordonare[2::3])
