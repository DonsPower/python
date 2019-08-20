datos = [5,6,7,8,9]
for i in range(0,5):
    print ( datos[i])
print

datos.remove(6)
for i in range(0, len(datos)):
    print  datos[i] ,
print

datos[0]=-2
for i in range(0,len(datos)):
    print ( datos[i]  ) ,
print

datos.insert(1,23)
for i in range(0,len(datos)):
    print ( datos[i]  ) ,
print

datos = datos + [31,32,33]
for i in range(0,len(datos)):
    print ( datos[i]  ) ,
print

x = range(3, 20, 3)
for n in x:
  print(n)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
