print("Ingresar dos numero:")
n1=int(input("Numero 1:"))
n2=int(input("Numero 2:"))
if n1==n2:
    print("Los 2 numeros son iguales")
elif n1>n2:
    print(f"El numero {n1} es mayor que {n2}")
else:
    print(f"El numero {n2} es mayor que {n1}")