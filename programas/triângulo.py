import math
print("Favor entrar com os dados em centímetros.")
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))
if a < b + c and b < a + c and c < a + b:
	x= (a+b+c)/2
	área= math.sqrt(x)*((x-a)*(x-b)*(x-c))
	print("Os segmentos formam um triângulo e sua área é:",área,"cm²")
else:
	print("Os segmentos",a,b,c," não formam um triângulo.")