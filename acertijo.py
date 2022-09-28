from random import randint

def llenarCajas():
    while (True):
        num=randint(0,99)
        encontrado=False
        for i in range(len(cajas)):
            if (cajas[i]==num):
                encontrado=True
                break
        if (encontrado==False):

            cajas.append(num)
        if (len(cajas)==100):
            break;

def buscarNumero(num):
    encontrado=False
    prisionero=num
    NumEnCaja=prisionero
    for i in range(0,50):
        if (cajas[NumEnCaja]==prisionero):
            return True
        else:
            NumEnCaja=cajas[NumEnCaja]
    return False

def lograronSalir():
    for i in range(0,100):
        if (buscarNumero(i)==False):
            return False
            break
    return True


contador=0
for i in range (0,100):
    cajas=[]
    llenarCajas()
    if (lograronSalir()):
        contador+=1
        
print("Cantidad de veces que lograron salir: ",contador)
