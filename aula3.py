print("Início da aula 3 (09/11/2023)")

contador = 1

while(contador <= 10):
  print(contador)
  contador = contador+1 #contador += 1

fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pêra"

frutas = ["morango", "laranja", "pêra"]

print(frutas)

print(frutas[2])

print(len(frutas)) 

frutas.append("manga")

print(len(frutas))
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])

print("Exemplo das frutas com while..")
frutas.append("uva")

i=0 
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo das frutas com FOR")
for fruta in frutas:
  print(fruta)