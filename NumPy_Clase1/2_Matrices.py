#MATRICES

import numpy as np

matriz = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(matriz)

print("\nPara obtener el numero de dimensiones(filas y columnas), usaremos elatributo 'ndim'")
print(matriz.ndim)

print("\nPara obtener el numero de elementos, usaremos 'size'")
print(matriz.size)

print("\nPara obtener la forma de un arreglo, use 'shape'")
tupla = matriz.shape
print(type(tupla), ':', tupla)
filas, columnas = tupla
print("La matriz tiene", filas,'filas y', columnas, 'columnas.', end ='\n\n')

print("""\nPara hacer slicing a una matriz, debemos señalar la posicion de la fila y columna en el 
siguiente orden: arreglo[fila, columna]""")
#Mostrar el elemento de la primera fila y primera columna de la matriz
print(matriz[0,0], end='\n\n')


print(matriz, end='\n\n')
#Mostar la primera fila
print(matriz[0, :], end='\n\n')

#Mostrar a partir de la segunda fila
print(matriz[1:, :],end='\n\n')

print("Podemos usar el método 'reshape' para cambiar la forma de arreglo")
vector = matriz.reshape((1,12))
print(vector)

print("'\nLa transpuesta de una matriz se calcula usando el atributo 'T' ")
transpuesta = matriz.T
print(transpuesta, end='\n\n')

print("""Para reordenar los elementos de una matriz en un solo vector, podemos 
utilizar la funcion 'flatten' """)
print(matriz.flatten())

#===============================================================
print('===============================================================')
print("AGRUPACION DE MATRICES")
print('===============================================================')

matriz_1 = np.array([[1,2,3], [4,5,6]])
matriz_2 = np.array([[7,8,9], [10,11,12]])

#Podemos agrupar las matrices horizontalmente con hstack
matrizz = np.hstack([matriz_1, matriz_2])
print(matrizz, end='\n\n')

#Podemos agrupar las matrices vertical con vstack
matrizzz = np.vstack([matriz_1,matriz_2])
print(matrizzz, end='\n\n')


