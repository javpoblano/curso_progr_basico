print("Calculadora")
print("1: Suma")
print("1: Resta")
print("1: Multiplicacion")
print("1: Division")

y = "2"
text = input("Ingrese la opcion")
op = int(text)

if(op==1):
	print("SUMA")
	val1 = int(input("valor 1:   "))
	val2 = int(input("valor 2:   "))
	print((val1+val2))
