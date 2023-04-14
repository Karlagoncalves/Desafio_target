def fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

def fibonacci_sequencia(num):
    sequencia = [0, 1]
    while sequencia[-1] < num:
        next_num = sequencia[-1] + sequencia[-2]
        sequencia.append(next_num)
    return sequencia

numero = int(input("Digite um número: "))
fibonacci = fibonacci_sequencia(numero)
if numero in fibonacci:
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")