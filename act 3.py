def cuadrado(l):
    area=l*l
    print("area del cuadrado ", area)

def triangulo(b,h):
    area=(b*h)/2
    print("area del triangulo ", area)
def circulo(r):
    area=3.14*(r*r)
    print("area del circulo ", area)
def sumatoria():
    i=0
    t=0
    limite=int(input("dame un numero entero(limite): "))
    for i in range(i,limite+1):
        if (i==limite):
            t=t+i
            print(limite,"= ", t)
            break
        t=t+i
        print(i,"+ ", end=" " )
seguir='s'
while(seguir=='s'):
    print("menu \n1.- area cuadrado, trianuglo, circulo\n2.-signo zodiacal\n3.-sumatoria")
    opc= int(input("escoge tu opcion: "))
    if opc==1:
        l=int(input("ingresa lado del cuadrado: "))
        cuadrado(l)
        b=int(input("ingresa base del triangulo: "))
        h=int(input("ingresa altura del triangulo: "))
        triangulo(b,h)
        r=int(input("ingresa radio del circulo: "))
        circulo(r)
    elif opc==2:
        d=int(input("ingresa tu dia de nacimineto: "))
        m=int(input("ingresa tu mes de nacimineto: "))
        if (d>=21 and m==1) or (d<=19 and m==2):
            print("acuario")
        elif d>=20 and m==2 or d<=20 and m==3:
            print("piscis")
        elif d>=21 and m==3 or d<=20 and m==4:
            print("aries")
        elif d>=21 and m==4 or d<=20 and m==5:
            print("tauro")
        elif d>=21 and m==5 or d<=21 and m==6:
            print("geminis")
        elif d>=22 and m==6 or d<=22 and m==7:
            print("cancer")
        elif d>=23 and m==6 or d<=23 and m==8:
            print("leo")
        elif d>=24 and m==8 or d<=22 and m==9:
            print("virgo")
        elif d>=23 and m==9 or d<=22 and m==10:
            print("libra")
        elif d>=23 and m==10 or d<=22 and m==11:
            print("escorpio")
        elif d>=23 and m==11 or d<=21 and m==12:
            print("sagitario")
        elif d>=22 and m==12 or d<=20 and m==1:
            print("capricornio") 
        
    elif opc==3:
        sumatoria()
    

        



    seguir=str(input("desea seguir con el programa 's' para si, 'n' para salir "))


