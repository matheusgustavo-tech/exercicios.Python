numb1 = float(input("Me fale um número: "))
numb2 = float(input("Me fale mais um número: "))
numb3 = float(input("Agora me fale o ultimo número: "))

if numb1 == numb2 == numb3:
    print("Os três números são idênticos")

else:
    print("Números digitados:", numb1, numb2, numb3)

    if numb1 <= numb2 and numb1 <= numb3:
        print("O menor número é:", numb1)

    elif numb2 <= numb1 and numb2 <= numb3:
        print("O menor número é:", numb2)

    else:
        print("O menor número é:", numb3)


