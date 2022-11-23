nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
genero = input("Informe seu genero: M = Masculino / F = Feminino / O = Outros: ")
print (f"Boa noite, o seu nome é: {nome}")
print("E sua idade é: {}".format(idade))

dobro = (idade * 2)
print("E o dobro da sua idade é: {}".format(dobro))

if idade >= 18 and genero == "M":
    print("Voce é maior de idade, pode dirigir ou beber, e vai ter que pegar exercito!")
else:
    print("Voce é maior de idade, pode dirigir ou beber!")
