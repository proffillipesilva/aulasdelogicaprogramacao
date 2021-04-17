def exemplo_basico(lista):

    print(len(lista))  #tamanho
    print(max(lista))  #valor maximo
    print(min(lista))  #valor minimo
    print(sum(lista))  #soma dos elementos
    print(sum(lista)/len(lista))  #media dos elementos

def exemplo_ordenacao(lista):
    for i in range(len(lista)):
        for j in range(i):
            if lista[j] > lista[i]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
lista = [3,4,1,2]
# exemplo_ordenacao(lista)

lista.sort() # valores crescentes
print(lista)
lista.reverse()
print(lista)



