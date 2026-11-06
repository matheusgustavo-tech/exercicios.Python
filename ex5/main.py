prec = float(input("Qual o valor do produto? "))

desconto = 0
percentual = 0
valor_final = 0

if prec < 0:
    print("Erro: valor inválido")

else:
    if prec < 100:
        percentual = 0

    elif prec < 200:
        percentual = 5
        desconto = prec * 5 / 100

    elif prec < 500:
        percentual = 10
        desconto = prec * 10 / 100

    else:
        percentual = 15
        desconto = prec * 15 / 100

    valor_final = prec - desconto

    print("Valor original:", prec)
    print("Percentual de desconto:", percentual, "%")
    print("Valor do desconto:", desconto)
    print("Valor final da compra:", valor_final)