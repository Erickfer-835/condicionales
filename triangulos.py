
n1=int(input("ingresa el primer lado "))
n2=int(input("ingresa el segundo lado "))
n3=int(input("ingresa el tercer lado "))


if n1 == n2 and n2 == n3:
        print ("el triangulo es equilatero")
elif n1==n2 or n1==n3 or n2==n3:
        print("el triangulo es isoseles")
else :
        print("el triangulo es escaleno")