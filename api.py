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
    for i in code:
        pprint.pprint(i)
        for j in i["energyData"]:
            pprint.pprint(j)


if __name__ == '__main__':
    print(buscar_dados())
