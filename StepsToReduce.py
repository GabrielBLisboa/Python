class Solution:
    def numberOfSteps(self, num: int) -> int:
        cont = 0
        while num != 0:
            if num % 2 == 0:
                cont += 1
                print("Passo", str(cont) + ")", num, "é par; dividido por 2 têm-se : ", num/2)
                num = num/2
            else:
                cont += 1
                print("Passo", str(cont) + ")", num, "é impar; subtraia 1 e terá: ", num-1)
                num -= 1
        return cont


num2 = int(input("Digite um número: "))
passos = Solution().numberOfSteps(num2)
print(passos)


