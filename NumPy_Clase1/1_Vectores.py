
#vectores

import numpy as np

print("\nAÑADIENDO VECTORES")
print("==================")
vector = np.array([1,2,3,4,5])
print(vector)

print("\nVECTOR ES DEL TIPO")
print("==================")
print(type(vector),'\n')

print("\n<Si queremos saber el tipo de informacion en cada posicion")
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
print(vector.dtype,'\n')

print("\nAñadirle FLOAT a los vectores")
print("=============================")
print(vector.dtype)
v= vector.astype(float)
print(v)
print(v.dtype)

print("\nImprimir unos componentes de un vector")
print(vector[0],'\n')
#Sacariamos el primer componente
print(vector[2:5])
#imprimira vector[2],vector[3],vector[4]
#Corresponde a 3,4,5 ----------Es igual a una lista 

print("\nSi queremos renombrar algun componente")
print("Antes",vector)
vector[-1]=10
#vector[-1]= 5 pero le estamos asignando un nuevo valor, en este caso el 10
#Comprobemos
print('dando un nuevo valor a vector[-1]:',vector)

print("\nCOPIAR UN VECTOR")
print("----------------")
print("antes de la copia:",vector)
copia= vector
print('copia',copia)


print("\nORDENAR LOS ELEMENTOS")
print("_____________________")
new_vector=np.array([5,2,3,7,1,6])
print(new_vector)

print("De menor a mayor")
ordenado = np.sort(new_vector)
print(ordenado)

print("De mayor a menor")
descendente = np.sort(new_vector)[::-1]
print(descendente)
