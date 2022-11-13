import numpy as np
import random
import random
def crear (a):
  lista =[]
  for i in range (a):
    i = random.random()
    lista.append(i)
    
  return lista 

#crear(7)

def crear_2(a,b,c):
  a = np.array(a)
  for i in range(a*b):
    i = crear(c)
    a.append (i)
  return a
a = crear_2(2,3,5)
print(a)