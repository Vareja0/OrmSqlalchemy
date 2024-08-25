#Riscala Miguel Fadel Neto
from itertools import product

txt = input("digite o nome do arquivo "); #o arquivo de texto deve estar na mesma pasta do programa, ou deve ser colocado o caminho absoluto do arquivo

arquivo = open(txt, "r") #abre o arquivo de texto
linhas = arquivo.readlines() #le todas as linhas e aloca em um array
total = int(linhas[0]) #define o total de operacoes como um inteiro

atual = 1  



for i in range(total):
    
    conjunto1 = set(linhas[atual + 1])
    conjunto2 = set(linhas[atual + 2])
    for item in conjunto1.copy(): #tira as virgulas, espacos e enters do array
        if item == ' ':
            conjunto1.remove(item)
        elif item == '\n':
            conjunto1.remove(item)
        elif item == ',':
            conjunto1.remove(item)

    for item in conjunto2.copy():
        if item == ' ':
            conjunto2.remove(item)
        elif item == '\n':
            conjunto2.remove(item)
        elif item == ',':
            conjunto2.remove(item)

    if ((linhas[atual]).strip().upper() == 'U'): #faz as operacoes de uniao, interseccao, diferenca e produto cartesiano
        final = conjunto1.union(conjunto2)
        print(f"Uniao: Conjunto 1 {conjunto1}, Conjunto 2 {conjunto2}. Resultado: {final}")
    elif ((linhas[atual]).strip().upper() == 'I'):
        final = conjunto1.intersection(conjunto2)
        print(f"Interseccao: Conjunto 1 {conjunto1}, Conjunto 2 {conjunto2}. Resultado: {final}")
    elif ((linhas[atual]).strip().upper() == 'D'):
        final = conjunto1.difference(conjunto2)
        print(f"Diferenca: Conjunto 1 {conjunto1}, Conjunto 2 {conjunto2}. Resultado: {final}")
    elif ((linhas[atual]).strip().upper() == 'C'):
        listas = [conjunto1, conjunto2]
        print(f"Produto Cartesiano: Conjunto 1 {conjunto1}, Conjunto 2 {conjunto2}. Resultado: ", end="")
        for elem in product(*listas):
            print(elem, end="")
        print("")
        
    atual += 3