
n1=int(input("ingresa el primer numero "))
n2=int(input("ingresa el segundo numero "))
n3=int(input("ingresa el tercer numero "))

if n1>n2 and n1>n3 and n2>n3:
    print("el ordesn es ",n1,n2,n3)
elif n1>n2 and n1>n3 and n3>n2:
    print("el orden es ",n1,n3,n2)
elif n2>n1 and n2>n3 and n1>n3:
    print("el orden es ",n2,n1,n3)
elif n1==n2 and n2>n3:
    print("el orden es ",n1,n2,n3)
elif n2>n1 and n2>n3 and n3>n1:
    print("el orden es ",n2,n3,n1)
elif n3>n1 and n3>n2 and n1>n2:
    print("el orden es ",n3,n1,n2)
elif n1==n3 and n1>n2:
    print("el orden es ",n1,n3,n2)
elif n1==n1 and n2>n3:
    print("el orden es ",n2,n1,n3)
else:
    print("el orden es ",n3,n2,n1)