# Programa simples de calculadora para demonstrar testes de unidade e CI/CD.

def somar(a, b):
    """Retorna a soma de a e b."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de b de a."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de a e b."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de a por b. Levanta ValueError se b for zero."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b

def potencia(base, expoente):
    """Retorna a base elevada ao expoente."""
    return base ** expoente
