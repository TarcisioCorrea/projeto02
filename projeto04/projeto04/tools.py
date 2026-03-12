import datetime

def data_atual():
    return datetime.date.today()


def calcular_idade(ano_nascimento):
    ano_atual = datetime.date.today().year
    return ano_atual - ano_nascimento


def converter_celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32