"""for linha in range(5):
    for coluna in range(5):
        print(f"[{linha} {coluna}]", end='')
    print('')
"""

linha0 = [1, 4, 6]
linha1 = [3, 8, 9]
linha2 = [0, 9, 3]
matriz = [linha0, linha1, linha2]

print(matriz)
print(matriz[2])
print(matriz[2][1])

for i in range(len(matriz)):
    linha = matriz[i]
    for j in range(len(linha)):
        print(f'{matriz[j][i]}', end=' ')
    print()

