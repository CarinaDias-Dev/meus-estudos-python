def  maior_num(*num):
        maior_elemento = lista[0]
        for n in lista[1:]:
            if n > maior_elemento:
                maior_elemento = n
        return maior_elemento


print(maior)