import requests
import json
import pprint


def buscar_dados():
    #request = requests.get("https://viacep.com.br/ws/04855450/json")
    request = requests.get(
        "https://devmonk-energymeter.herokuapp.com/EnergyMeter")
    pprint.pprint(json.loads(request.content))


if __name__ == '__main__':
    buscar_dados()
