cost = float(input("Ingresar gasto:"))
print(cost)
money = float(input("Dinero recibido"))
print(money)

Pesos = money - cost

print("\n""Vuelto")

print("\n""Pesos:")
print(Pesos)

print("Centavos:")
centavos = (Pesos - (int(Pesos)))
print(int(centavos*100))