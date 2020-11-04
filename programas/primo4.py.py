num = int(input("Digite o valor de n (n > 0): "))

if num == 2 or (num != 1 and num % 2 == 1):
	éprimo = True
else:
	éprimo = False

divisor = 3

while divisor < num and éprimo:
	if num % divisor == 0:
		éprimo = False
	divisor += 2
if éprimo:
	print("é primo")
else:
	print("não primo")
