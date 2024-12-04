
def soma(a, b):
    if b == 0:
        return a
    if b > 0:
        return soma(a + 1, b - 1)
    return soma(a - 1, b + 1)


def subtracao(a, b):
    if b == 0:
        return a
    if b > 0:
        return subtracao(a - 1, b - 1)
    return subtracao(a + 1, b + 1)


def multiplicacao(a, b): #chama funcao soma n vezes p fazer a multiplicacao
    if b == 0:
        return 0
    return soma(a, multiplicacao(a, b - 1))


def divisao_inteira(a, b): #chama funcao subtracao n vezes p fazer a divisao
    if a < b:
        return 0
    return soma(1, divisao_inteira(subtracao(a, b), b))


def resto_divisao(a, b): #retorna a sobra
    if a < b:
        return a
    return resto_divisao(subtracao(a, b), b)


def exponencial(base, expoente):
    if expoente == 0: # faz a subtracao recursiva para encontrar o expoente
        return 1
    resultado_parcial = exponencial(base, subtracao(expoente, 1))
    soma_resultado = 0
    for _ in range(base): #faz a soma recursiva para a base
        soma_resultado = soma(soma_resultado, resultado_parcial)
    return soma_resultado

# subtrai 1 de n a cada chamada recursiva e somando os resultados parciais
def fatorial(n):
    if n == 0:
        return 1
    return multiplicacao(n, fatorial(subtracao(n, 1)))


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # soma recursiva p dois números anteriores (n-1 e n-2) para formar o próximo número
    fib_n_minus_1 = fibonacci(subtracao(n, 1))
    fib_n_minus_2 = fibonacci(subtracao(n, 2))
    return soma(fib_n_minus_1, fib_n_minus_2)

def menu():
    print("\nSelecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão Inteira")
    print("5 - Resto da Divisão")
    print("6 - Exponencial")
    print("7 - Fatorial")
    print("8 - Fibonacci")
    print("0 - Sair")

while True:
    menu()
    escolha = input("Digite sua escolha: ")

    try:
        if escolha == "0":
            print("Encerrando o programa.")
            break

        elif escolha in {"1", "2", "3", "4", "5"}:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))

            if escolha == "1":
                print(f"Resultado: {soma(num1, num2)}")
            elif escolha == "2":
                print(f"Resultado: {subtracao(num1, num2)}")
            elif escolha == "3":
                print(f"Resultado: {multiplicacao(num1, num2)}")
            elif escolha == "4":
                quociente = divisao_inteira(num1, num2)
                resto = resto_divisao(num1, num2)
                print(f"Resultado: Quociente = {quociente}, Resto = {resto}")
            elif escolha == "5":
                print(f"Resultado: {resto_divisao(num1, num2)}")

        elif escolha == "6":
            num = int(input("Digite o número: "))
            print(f"Resultado: {exponencial(num1, num)}")

        elif escolha == "7":
            num = int(input("Digite o número: "))
            print(f"Resultado: {fatorial(num)}")

        elif escolha == "8":
            num = int(input("Digite o número: "))
            print(f"Resultado: Fibonacci({num}) = {fibonacci(num)}")

        else:
            print("Escolha inválida. Tente novamente.")

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
