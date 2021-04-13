import requests
import json
import pprint

lista_arquivo = []


def buscar_dados():
    # request = requests.get("https://viacep.com.br/ws/04855450/json")
    request = requests.get(
        "https://devmonk-energymeter.herokuapp.com/EnergyMeter")
    x = request.json()
    return client_code(x)


def client_code(code):
    # pprint.pprint(code)
    x = int(code[0]["clientCode"])
    y = str(x)
    tamanho = len(str(x))

    if tamanho < 10:
        x = y.zfill(10)
    return cep_code(code, x)


def cep_code(code, linha):
    x = code[0]["zipCode"]
    cep = x.replace("-", "")
    y = linha + cep
    print(y)
    return complement_code(code, y)


def complement_code(code, linha):
    pass


if __name__ == '__main__':
    pprint.pprint(buscar_dados())
