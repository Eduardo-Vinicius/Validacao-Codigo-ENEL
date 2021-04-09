import requests
import json


def buscar_dados():
    #request = requests.get("https://viacep.com.br/ws/04855450/json")
    request = requests.get(
        "https://devmonk-energymeter.herokuapp.com/EnergyMeter")
    print(json.loads(request.content))


if __name__ == '__main__':
    buscar_dados()

