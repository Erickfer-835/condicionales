edad=int(input("dime la edad del cliente: "))

if edad in range (0,13):
    print("van a ser 50 pesos")
elif edad in range(13,17):
    print("van a ser 80 pesos")
else:
    print("van a ser 120")