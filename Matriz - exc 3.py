matriz = []

for i in range(5):
    linha = []
    
    m = int(input("Matricula: "))
    linha.append(m)
    
    p = int(input("Media das provas: "))
    linha.append(p)
    
    t = int(input("Media dos trabalhos: "))
    linha.append(t)
    
    nf = p + t
    linha.append(nf)
    
    matriz.append(linha)

maior = matriz[0][3]
aluno = matriz[0][0]

for i in range(5):
    if matriz[i][3] > maior:
        maior = matriz[i][3]
        aluno = matriz[i][0]

print("\nMatricula de maior media:",aluno)