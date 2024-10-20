# TODO Найдите количество книг, которое можно разместить на дискете

size = 1.44 #mb
stranic = 100
strok = 50
simvolov = 25
size_simvola = 4 #байта

size_knigi = simvolov * strok * stranic * size_simvola
size1 = size * 1024 **2
count = round(size1 // size_knigi)

print("Количество книг, помещающихся на дискету:", count)