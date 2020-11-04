n1= float(input("Primeiro número: "))
n2= float(input("Segundo número: "))
n3= float(input("Terceiro número: "))

menor= n1

if (n1<n2) and (n1<n3):
	menor= n1
if (n2<n1) and (n2<n3):
	menor= n2
else:
	menor= n3

print("O menor número é:",menor,)
