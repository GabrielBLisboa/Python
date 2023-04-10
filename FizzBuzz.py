class Solution:
    def fizzBuzz(n: int) -> list[str]:
        return [(not i % 3) * "Fizz" + (not i % 5) * "Buzz" or str(i) for i in range(1, n + 1)]


"""
        return [str(i) if (i % 3 != 0 and i % 5 != 0) else \
                (('Fizz' * (i % 3 == 0)) + ('Buzz' * (i % 5 == 0))) \
                for i in range(1, n + 1)]
"""
""" 
        lista = []
        for x in range(1, n+1):
            if x % 3 == 0 and x % 5 == 0:
                lista.append("FizzBuzz")
            elif x % 3 == 0:
                lista.append("Fizz")
            elif x % 5 == 0:
                lista.append("Buzz")
            else:
                lista.append(x)
        return lista
"""

num = int(input("Digite o numero: "))
exec = Solution()
result = Solution.fizzBuzz(num)
print(result)