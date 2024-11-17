def email_valido(email):
    return "@" in email and "." in email


def dividir(a, b):
    if b == 0:
        return None
    return a / b


def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


def verificade_idade(idade):
    if idade < 18:
        raise ValueError("Acesso negado para menores de 18 anos")

    return "Acesso permitido"


def dividir_com_raise(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b
