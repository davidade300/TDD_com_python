def classifica_idade(idade):
    if idade < 13:
        return "Crianca"
    elif idade < 20:
        return "Adolescente"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"
