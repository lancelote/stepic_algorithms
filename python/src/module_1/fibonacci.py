"""
Дано целое число 1≤𝑛≤40, необходимо вычислить 𝑛-е число Фибоначчи (напомним,
что 𝐹0=0, 𝐹1=1 и 𝐹𝑛=𝐹𝑛−1+𝐹𝑛−2 при 𝑛≥2).
"""


def fibonacci(n):
    """Calculate the given Fibonacci number.

    Examples:

        >>> fibonacci(8)
        21
    """
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a
