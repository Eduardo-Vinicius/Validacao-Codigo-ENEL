import requests
import json
import pprint

lista_arquivo = []
dic_mes = {
    "01":"Janeiro   ", 
    "02":"Fevereiro ", 
    "03":"Março     ", 
    "04":"Abril     ", 
    "05":"Maio      ", 
    "06":"Junho     ",
    "07":"Julho     ", 
    "08":"Agosto    ", 
    "09":"Setembro  ", 
    "10":"Outubro   ", 
    "11":"Novembro  ", 
    "12":"Dezembro  "   
}

def buscar_dados():
    # request = requests.get("https://viacep.com.br/ws/04855450/json")
    request = requests.get(
        "https://devmonk-energymeter.herokuapp.com/EnergyMeter")
    x = request.json()
    return x


def client_code(code):
    # pprint.pprint(code)
    x = int(code["clientCode"])
    y = str(x)
    tamanho = len(str(x))

    if tamanho < 10:
        x = y.zfill(10)
    return cep_code(code, x)


def cep_code(code, linha):
    x = code["zipCode"]
    cep = x.replace("-", "")
    y = linha + cep
    return number_code(code, y)

def number_code(code, linha):
    x = code["addressNumber"]
    tamanho = len(x)

    if tamanho < 10 :
        x = x.zfill(5)
    
    return complement_code(code, linha + x )


def complement_code(code, linha):
    x = str(code["complement"])
    x = x.ljust(20, " ")
    return regiao_code(code, linha + x)

def regiao_code(code,linha):
    return energy_code(code,linha + "##SSP")


def energy_code(code, linha):
    x = code["energyData"]
    for i in x:
        device = str(i["device"])
        device = device.zfill(2)

        medidor = str(i["energyMeterCode"])
        medidor = medidor.zfill(10)

        kw = i["kiloWatss"]

        custo = 0.30 * kw
        custo = format(float(custo), '.2f')

        kw = str(i["kiloWatss"])
        kw = kw.zfill(6)

        data = i["measureDate"]
        data = data.replace("-","")
        data = data.replace("T","")
        data = data.replace(":","")

        dia = data[6:8]
        mes = str(data[4:6])
        mes = dic_mes[mes]
        ano = data[0:4]
        hora = data[8:10]
        minuto = data[10:12]
        segundo = data[12:14]

        custo = str(custo)
        custo = custo.replace(".", "")
        custo = custo.zfill(7)
        energydata =  dia + mes + ano + hora + minuto + segundo + medidor + device + kw + custo
        y = linha + energydata
        lista_arquivo.append(y)

    return lista_arquivo

   #pprint.pprint(code[0])


def preenche_arquivo(lista):
    with open('invoice.data', 'w') as arquivo:
        for i in lista:
            arquivo.write(i + "\n")



if __name__ == '__main__':
    x = buscar_dados()
    for i in x:
        client_code(i)
    preenche_arquivo(lista_arquivo)
