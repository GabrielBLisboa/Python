contas = [[2,8,7],[7,1,3],[1,9,5]]
maisrico = 0


def wealth (contas2):
    soma=0
    for i in contas2:
        total=sum(i)
        soma=max(soma,total)
    return soma

maisrico = wealth(contas)
print(maisrico)