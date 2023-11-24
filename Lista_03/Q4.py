N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())
    if Y != 0:
        # Calcula e imprime o resultado da divisão com um dígito após o ponto decimal
        resultado = X / Y
        print(f"{resultado:.1f}")
    else:
        # Se Y for igual a zero, imprime "divisao impossivel"
        print("divisao impossivel")