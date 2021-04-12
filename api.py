import requests
import json
import pprint


def buscar_dados():
    # request = requests.get("https://viacep.com.br/ws/04855450/json")
    request = requests.get(
        "https://devmonk-energymeter.herokuapp.com/EnergyMeter")
    x = request.json()
    return client_code(x)


def client_code(code):
    x = str(code[0]["clientCode"])
    tamanho = len(str(x))

    if tamanho < 10:
        dif = 10 - tamanho
        x = x.zfill(dif)
    return x


if __name__ == '__main__':
    pprint.pprint(buscar_dados())
