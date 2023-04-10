dic1 = {'L':50, 'X':10, 'V':5, 'I':1}

def verifica(char):
    num2 = dic1[char]
    return num2

letras = input("Digite o número romano: ")
letras2=letras.split()
num1 = list(map(verifica, *letras2))
i = 0
while i < len(num1):
    if num1[i] > (num1[i - 1]) and i!=0:
         num1[i] = num1[i]-(num1[i-1]*2)
    i+=1
num3=sum(num1)
print(num3)


