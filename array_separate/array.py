""" Segundo Ejercicio Prueba Tecnica Habi - Array"""
"""Definir el array a revisar"""
myArray = [1, 3, 2, 0, 7, 8, 1, 3, 0, 0, 6, 0, 0, 7, 1]

blocks = []
current_block = []

for num in myArray:
    if num == 0:
        # Fin de un bloque de numeros
        if current_block:
            sorted_block = ''.join(str(n) for n in sorted(current_block))
            blocks.append(sorted_block)
        else:
            blocks.append("X")
        current_block = []
    else:
        current_block.append(num)

# Agregar ultimo bloque si este existe
if current_block:
    sorted_block = ''.join(str(n) for n in sorted(current_block))
    blocks.append(sorted_block)
else:
    blocks.append("X")

# Imprimir el resultado
print(' '.join(blocks))
