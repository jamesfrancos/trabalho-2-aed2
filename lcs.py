import time

def lcs(item1,item2):
    maior = []
    menor = []

    if(len(item1)>len(item2)):
        maior = item1
        menor = item2
    else:
        maior = item2
        menor = item1
    
    def guloso(caminho,i,j):
        if(i==len(menor) or j==len(maior)):
            return caminho

        if(menor[i] == maior[j]):
            caminho.append(menor[i])
            return guloso(caminho,i+1,j+1)
        else:
            return guloso(caminho,i,j+1)


    return guloso([],0,0)


X = "ABCBDAB"
Y = "BDCAB"
inicio = time.perf_counter()
Z = lcs(X,Y)
fim = time.perf_counter()
tempoTotal = fim - inicio
print(Z)
print(f"tempo total:{tempoTotal:.6f} segundos")
