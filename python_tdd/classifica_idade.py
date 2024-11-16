def classifica_idade(idade):
    if idade < 12:
        return "Crianca"
    elif idade < 18:
        return "Adolescente"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"
