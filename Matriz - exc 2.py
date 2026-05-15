matriz = []

print("Digite os 16 valores da matriz 4x4:")

for i in range (4):
    linha = []
    for j in range (4):
        num = int(input(f"Linha {i+1}, coluna {j+1}:"))
        linha.append(num)
    matriz.append(linha)

print("\nMatriz:")
for linha in matriz:
    print(linha)

maior = matriz[0][0]   
linha_maior = 0
coluna_maior = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print("\nO maior valor é:",maior)