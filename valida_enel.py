import re
import pprint


lista_texto = ["00000348340483300100051Bloco 1A apto 44    ##SSP29Dezembro  20211544230007A16894030000840001550",
               "000103483404833001sd00051Bloco 1A apto 44    ##SSP29Fevereiro 20211544230007A168940300020240001550",
               "00000348340483300100051Blsoo 1A apto 44    ##MMG19Março    20211544230007A16894030000840042550",
               "00000348340483300100051Bloco 2B apto 44    ##SSP29Fevereiro 20211544230007A16894030000840001550",
               "000003232340483300100051Bloco 1A apto 44    ##SSP22Fevereiro 20211544230007A16894030000840001550",
               "00000348340483300100051Bloco 1A apto 44    ##SSP29Fevereiro 2022544230007A16894330000840001550",
               "00000R540483300100051Bloco 1A apto 44    ##SSP32Fevereiro 20211544230007A16894030000840001550",
               "000003483404832310100051Bloco 1A apto 44    ##SSP29Fevereiro 20211544230007A168940300034840001550",
               "000003483404833033330051Bloco 1A apto 44    #SSP29F232 21154330007A16894030000840001550",
               "00000348340483300100051Bloco 1A   ##SSP29Fevereiro 20211544230007A1689403000240001550",
               "00000348340481100051Bloco 1A apto 44    ##SSP29Fevereiro 2022244230007A16894030000840001550",
               "00O00348340483E00100051Bloco 1A a.to 44    ##S5P29Feveeir0 20211544230007A168940300008400015@0",
               "00O00348340483E00100051Bloco 1A apto 999    ##S5P29Fev3eir0 20211544230007A1689403000084015@0",
               "00000348340483300100051Bloco 1A apto 44    ##SSP29Junh0     00211544230007A16894030000840001550",
               "00000348340483300100000Bloco 1A apto 00    ##SSP29Fevereiro 20211544230007A16894030000840001550",
               "00000000000000000100051Bloco 1A apto 44    ##SSP29Fevereiro 20211544230007A16894030000840001550",
               "99O00348340483E00100051Bloco 12 apt0 44    *#S5P29Feve&eir0 20211544230007A168940300008400019950",
               "000003483404833001000Bloco 1A apto 44    ##SSP29Fevereiro 20211544230007A16894030000840001550",
               "00000348340483300100051Bloco 1A apto 44    ##SSP29julia 20211544230007A16894030000840001550"]

# texto_enel = "00000348340483300100051Bloco 1A apto 44    ##SSP29Fevereiro 20211544230007A16894030000840001550"

lista_show_error = []


def show_error(line, error, field):
    x = f"Na linha {line} do arquivo, aconteceu o erro: '{error}' no campo {field}"
    lista_show_error.append(x)
    return f"Na linha {line} do arquivo, aconteceu o erro: '{error}' no campo {field}"

# print(x)

# print(len(texto_enel))
# print(texto_enel[10:18])


lista = ["Janeiro   ", "Fevereiro ", "Março     ", "Abril     ", "Maio      ", "Junho     ",
         "Julho     ", "Agosto    ", "Setembro  ", "Outubro   ", "Novembro  ", "Dezembro  "]

erros = {
    "tamanho": "O tamanho da linha se encontra incorreto!",
    "nao_zero": "Os caracteres informados são todos 0!",
    "value_error": "O campo não contém apenas números.",
    "special_char": "O campo contém caracteres especiais.",
    "regiao_hash": "A Região não possui '##' como complemento.",
    "regiao_code": "O código da Região está incorreto!",
    "invalid_value": "Valor inválido!",
    "space": "Não pode possuir espaços no campo."
}

aparelhos = {
    "01": "Aspirador",
    "02": "Batedeira",
    "03": "Carregador de Celular",
    "04": "Chuveiro",
    "05": "Computador",
    "06": "Geladeira",
    "07": "Liquidificador",
    "08": "Máquina de Lavar",
    "09": "Microondas",
    "10": "Secadora",
    "11": "Secador de Cabelo",
    "12": "Televisão",
    "13": "Vassoura Elétrica",
    "14": "Outros"
}

# print(aparelhos["01"])


def valida_tamanho(texto, linha):
    tamanho = len(texto)
    if tamanho > 95 or tamanho < 95:
        show_error(linha, erros["tamanho"], "Tamanho")
        dic_erros[linha].append(erros["tamanho"])
    return valida_cliente(texto, linha)


def valida_cliente(texto, linha):
    if texto[0:10] == "0000000000":
        show_error(linha, erros["nao_zero"], "Cliente")
        dic_erros[linha].append(
            erros["nao_zero"])
    cliente = converte_numero(texto[0:10])
    if is_int(cliente) != True:
        show_error(linha, erros["invalid_value"], "Cliente")
        dic_erros[linha].append(
            "Cliente: Encontrado problema no código do cliente!")
    valida_cep(texto, linha)


def valida_cep(texto, linha):
    cep = texto[10:18]
    if cep == "00000000":
        show_error(linha, erros["nao_zero"], "CEP")
        dic_erros[linha].append(erros["nao_zero"])
    cep = converte_numero(cep)
    if is_int(cep) != True:
        dic_erros[linha].append(
            erros["value_error"])
    valida_numero(texto, linha)


def valida_numero(texto, linha):
    numero = texto[18:23]
    if numero == "00000":
        show_error(linha, erros["nao_zero"], "Número: ")
        dic_erros[linha].append(
            erros["nao_zero"])
    if contains_special(numero) == True:
        show_error(linha, erros["special_char"], "Número: ")
        dic_erros[linha].append(
            erros["special_char"])
    valida_complemento(texto, linha)


def valida_complemento(texto, linha):
    complemento = texto[23:42]
    if is_int(complemento) == True:
        show_error(linha, erros["special_char"], "Complemento: ")
        dic_erros[linha].append(
            "Complemento - O complemento só possui números")
    if contains_special(complemento) == True:
        show_error(linha, erros["special_char"], "Complemento: ")
        dic_erros[linha].append(
            erros["special_char"])
    valida_regiao(texto, linha)


def valida_regiao(texto, linha):
    regiao = texto[43:48]
    if regiao[0:2] != "##":
        show_error(linha, erros["special_char"], "Região: ")
        dic_erros[linha].append(
            erros["regiao_hash"])
    if regiao[2:5] != "SSP":
        show_error(linha, erros["regiao_code"], "Região: ")
        dic_erros[linha].append(erros["regiao_code"])
    valida_dia(texto, linha)


def valida_dia(texto, linha):
    dia = texto[48:50]
    idia = converte_numero(dia)
    if is_int(idia) == False:
        show_error(linha, erros["special_char"], "Dia: ")
        dic_erros[linha].append(erros["value_error"])
    if idia == 0 or idia > 31:
        show_error(linha, erros["invalid_value"], "Dia: ")
        dic_erros[linha].append(erros["invalid_value"])
    valida_mes(texto, linha)


def valida_mes(texto, linha):
    mes = texto[50:60]

    for i in lista:
        if mes not in lista:
            show_error(linha, erros["invalid_value"], "Mês: ")
            dic_erros[linha].append("Não encontramos o mês na lista")
            break
    valida_ano(texto, linha)


def valida_ano(texto, linha):
    ano = texto[60:64]

    if ano == "0000":
        dic_erros[linha].append(erros["nao_zero"])
    if contains_special(ano) == True:
        show_error(linha, erros["special_char"], "Ano")
        dic_erros[linha].append(erros["special_char"])
    ano = converte_numero(ano)
    if is_int(ano) == False:
        show_error(linha, erros["value_error"], "Ano")
        dic_erros[linha].append(erros["value_error"])

    valida_hora(texto, linha)


def valida_hora(texto, linha):

    hora = converte_numero(texto[64:66])
    if hora > 23 or hora < 0:
        show_error(linha, erros["invalid_value"], "Hora")
        dic_erros[linha].append(erros["invalid_value"])
    valida_minuto(texto, linha)


def valida_minuto(texto, linha):
    minuto = texto[66:68]
    if contains_special(minuto) == True:
        show_error(linha, erros["special_char"], "Minuto")
        dic_erros[linha].append(erros["special_char"])
    minuto = converte_numero(texto[66:68])

    if minuto > 59 or minuto < 0 or minuto == False:
        show_error(linha, erros["invalid_value"], "Minuto")
        dic_erros[linha].append(erros["invalid_value"])

    valida_segundo(texto, linha)


def valida_segundo(texto, linha):
    segundo = texto[68:70]
    if contains_special(segundo) == True:
        show_error(linha, erros["special_char"], "Segundo")
        dic_erros[linha].append(erros["special_char"])
    segundo = converte_numero(texto[68:70])
    if segundo > 59 or segundo < 0:
        show_error(linha, erros["invalid_value"], "Segundo")
        dic_erros[linha].append(erros["invalid_value"])

    valida_medidor(texto, linha)


def valida_medidor(texto, linha):
    medidor = texto[70:79]
    if medidor.isspace() == True:
        show_error(linha, erros["space"], "Medidor")
        dic_erros[linha].append("Medidor - O medidor não deve possuir espaços")
    if medidor == "0000000000":
        show_error(linha, erros["nao_zero"], "Medidor")
        dic_erros[linha].append(erros["nao_zero"])
    valida_aparelho(texto, linha)


def valida_aparelho(texto, linha):
    aparelho = converte_numero(texto[80:82])
    if aparelho > 14 or aparelho <= 0:
        show_error(linha, erros["invalid_value"], "Aparelho")
        dic_erros[linha].append(erros["invalid_value"])
    valida_kw(texto, linha)


def valida_kw(texto, linha):
    kw = texto[82:87]
    if contains_special(kw):
        show_error(linha, erros["special_char"], "KW")
        dic_erros[linha].append(erros["special_char"])

    kw = converte_numero(texto[82:87])
    if is_int(kw) == False:
        show_error(linha, erros["value_error"], "KW")
        dic_erros[linha].append(erros["value_error"])
    if kw == "000000":
        show_error(linha, erros["nao_zero"], "KW")
        dic_erros[linha].append(erros["nao_zero"])

    valida_custo(texto, linha)


def valida_custo(texto, linha):
    custo = texto[88:95]
    x = custo[0:5] + "." + custo[5:7]
    if custo == "":
        show_error(linha, "Custo - Não possui caracteres", "Custo")
        dic_erros[linha].append("Custo - Não possui caracteres")
    else:
        if contains_special(x) == True:
            show_error(linha, erros["special_char"], "Custo")
            dic_erros[linha].append(erros["special_char"])
        else:
            x = float(x)
            if x <= 0:
                show_error(
                    linha, "Custo - O Custo não pode ser zero ou negativo", "Custo")
                dic_erros[linha].append(
                    "Custo - O Custo não pode ser zero ou negativo")


def converte_numero(x):
    try:
        return int(x)
    except ValueError:
        return False


def converte_decimal(x):
    try:
        return float(x)
    except ValueError:
        print("O texto não contém apenas números")
        return False


def is_float(x):
    if type(x) == float:
        return True
    return False


def is_int(x):
    if type(x) == int:
        return True
    return False


def contains_special(texto):
    string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if(string_check.search(texto) == None):
        return False
    return True


dic_erros = {}

if __name__ == "__main__":
    tamanho = len(lista_texto)
    contador = 1
    for i in lista_texto:
        dic_erros[contador] = [""]
        valida_tamanho(i, contador)
        contador += 1


pprint.pprint(lista_show_error)
pprint.pprint(dic_erros)
