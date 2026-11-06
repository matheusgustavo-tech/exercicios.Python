quantidade = 0
soma = 0
numero = float(input("Me informe um numero "))

while numero != 0:
 quantidade = quantidade + 1
 soma = soma + numero

 numero = float(input("Digite outros número:"))

print('Quantidade de número:', quantidade)
print("Soma total:", soma)