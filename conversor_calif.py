calif=int(input("dime la calificacion: "))

if calif in range(90,101):
    print("la calif es A")
elif calif in range(80,90):
    print("la calif es B")
elif calif in range(70,80):
    print("la calif es C")
elif calif in range(60,70):
    print("la calif es D")
else:
    print("la calif es F")