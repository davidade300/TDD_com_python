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
