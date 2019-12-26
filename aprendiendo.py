import turtle
import calendar
import time


def mifunction():
    print("Hola esto es una funcion")
    print(calendar.weekheader(8))
    print(calendar.firstweekday())
    print(calendar.month(2019, 8))
    print(calendar.monthcalendar(2019, 8))
    print(calendar.calendar(2019))


def loopif():
    #If
    a = 56
    b = 66
    if a > b:
        print("hola")
    elif a == b:
        print("iguales")
    else:
        print("Este no es igual")


def loopwhile():
    #con string
    nom = "al"
    cont = 0
    while nom != "aaaa":
        nom += "a"

        print(nom)
        cont += 1
        if nom == "alaa":
            break
    return cont


def loopfor():
    for x in range(10, 1, -1):
        print(x)


#Datos primitivos
#enteros,string float
#casteo
def casteo():
    print(str(1) + "Hola")
    print(int("343") + 7)


def tiposdedato():
    #String
    s = "Hola mundo {i} {j}"
    print(s.format(i=12, j=2))


def duplasList():
    #En la lista puede ir cualquier tipo de dato.
    i = [1, 5, 3]
    print(i)
    i.append(3)
    i.sort()
    i.reverse()
    a = i.count(3)
    print(i)
    a = "first time"
    b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #print ("El numero dos se repite: "+str(a)+"junto con el: "+str(a))
    print(i[1:2])
    print(a[:3])
    #Se puede de reversa tambien.
    print(b[10:0:-2])
    c = b[::-1]
    print(c)
    for x in range(len(b)):
        print(b[0:x])


def tuplas():
    i = ("Monica", 21, 120)
    name,age,money=i
    x,bol=21,True
    print(x)
def splitandjoin():
  a="Hola hace"
  l=a.split(" ")
  print(l)
  #joined
  joined=" que ".join(l)
  print(joined)
def seet():
  #Elimina los repetitivos
  i=[1,2,3,3,3,4,5,6,51]
  a=set(i)
  print(a)
def muta():
  i=[1,2,[3,4]]
  print (i)
  i[2][0]=7
  print(i)
  j=[0][0]
  for x in range(1,10):
    for y in range(1,10):
      j.append(y)
    j.append(x)


#mifunction()
#print(loopwhile())
#loopfor()
#casteo()
#tiposdedato()
#duplasList()
#tuplas()
#splitandjoin()
#seet()
muta()
