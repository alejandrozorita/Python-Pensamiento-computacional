def fibonacci(n):
    print(n)
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('dame un número: '))

print(f'el resultado es: {fibonacci(n)}')