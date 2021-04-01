import re

lista_texto = ["00000348340483300100051Bloco 1A apto 44    ##SSP29Fevereiro 20211544230007A16894030000840001550",
               "000103483404833001sd00051Bloco 1A apto 44    ##SSP29Fevereiro 20211544230007A168940300020240001550",
               "00000348340483300100051Blsoo 1A apto 44    ##MMG19Março    20211544230007A16894030000840042550"]

# texto_enel = "00000348340483300100051Bloco 1A apto 44    ##SSP29Fevereiro 20211544230007A16894030000840001550"


def show_error(line, error, field):
    return f"Na linha {line} do arquivo, aconteceu o erro: '{error}' no campo {field}"


x = show_error(1, "xablau", "febem")
print(x)

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

print(aparelhos["01"])


def valida_tamanho(texto):
    tamanho = len(texto)
    if tamanho > 95 or tamanho < 95:
        print("tamanho incorreto, o código informado se encontra com erro!")
    return valida_cliente(texto)


def valida_cliente(texto):
    if texto[0:10] == "0000000000":
        print("*Erro no Cliente* - Os números não podem ser 0! Erro no cliente!")
    cliente = converte_numero(texto[0:10])
    if is_int(cliente) != True:
        print("*Erro no Cliente* - Encontrado problema no código do cliente!")
    else:
        valida_cep(texto)


def valida_cep(texto):
    cep = texto[10:18]
    if cep == "00000000":
        print("*Erro no CEP* -  O Cep contém apenas o número 0 (Zero).")
    cep = converte_numero(cep)
    if is_int(cep) != True:
        print("*Erro no CEP* - O Cep está incorreto, não contém apenas números!")
    else:
        valida_numero(texto)


def valida_numero(texto):
    numero = texto[18:23]
    if numero == "00000":
        print("*Erro no Número* - O número não pode conter apenas 0 Zero.")
    if contains_special(numero) == True:
        print("*Erro no Número* - O número contém caracteres especiais!")
    else:
        valida_complemento(texto)


def valida_complemento(texto):
    complemento = texto[23:42]
    if is_int(complemento) == True:
        print("*Erro no Complemento* - O complemento só possui números")
    if contains_special(complemento) == True:
        print("*Erro no Complemento* - O complemento não pode possuir caracter especial")
    else:
        valida_regiao(texto)


def valida_regiao(texto):
    regiao = texto[43:48]
    if regiao[0:2] != "##":
        print("*Erro na Região* - A Região não possui '##' como complemento")
    if regiao[2:5] != "SSP":
        print("*Erro na Região* - O Codigo da Região não é valido")
    else:
        valida_dia(texto)


def valida_dia(texto):
    dia = texto[48:50]
    idia = converte_numero(dia)
    if is_int(idia) == False:
        print("*Erro no Dia* - O dia não é um número")
    if idia == 0 or idia > 31:
        print("*Erro no Dia* - Esse dia não é valido")
    else:
        valida_mes(texto)


def valida_mes(texto):
    mes = texto[50:60]
    for i in lista:
        if mes not in lista:
            print("Não encontramos o mês na lista")
    print("Tudo ok")
    valida_ano(texto)


def valida_ano(texto):
    ano = texto[60:64]

    if ano == "0000":
        print("*Erro no Ano* - O ano não pode ser somento '0'")
    if contains_special(ano) == True:
        print("*Erro no Ano* - O ano não pode possuir caracteres especiais")
    ano = converte_numero(ano)
    if is_int(ano) == False:
        print("*Erro no Ano* - O ano deve possuir somente números")

    else:
        valida_hora(texto)


def valida_hora(texto):
    hora = converte_numero(texto[64:66])
    if hora > 23 or hora == 0:
        print("*Erro na Hora* - A Hora não é valida")
    else:
        valida_minuto(texto)


def valida_minuto(texto):
    minuto = texto[66:68]
    if contains_special(minuto) == True:
        print("*Erro no Minuto* - O Minuto não pode Possuir um caractere especial")
    minuto = converte_numero(texto[66:68])
    if minuto > 59 or minuto < 0:
        print("*Erro no Minuto* - O Minuto não é valido")

    else:
        valida_segundo(texto)


def valida_segundo(texto):
    segundo = texto[68:70]
    if contains_special(segundo) == True:
        print("*Erro no Segundo* - O Segundo não pode Possuir um caractere especial")
    segundo = converte_numero(texto[68:70])
    if segundo > 59 or segundo < 0:
        print("*Erro no Segundo* - O Segundo não é valido")

    else:
        valida_medidor(texto)


def valida_medidor(texto):
    medidor = texto[70:79]
    if medidor.isspace() == True:
        print("*Erro no Medidor* - O medidor não deve possuir espaços")
    if medidor == "0000000000":
        print("*Erro no Medidor* - O medidor não pode possuir somente zeros")
    else:
        valida_aparelho(texto)


def valida_aparelho(texto):
    aparelho = converte_numero(texto[80:82])
    print(aparelho)
    if aparelho > 14 or aparelho <= 0:
        print("*Erro no Aparelho* - Esse Aparelho não é valido")
    else:
        valida_kw(texto)


def valida_kw(texto):
    kw = texto[82:87]
    if contains_special(kw):
        print("*Erro no KW* - O kw não deve conter caracteres especiais")

    kw = converte_numero(texto[82:87])
    if is_int(kw) == False:
        print("*Erro no KW* - O kw deve conter somente numeros")
    if kw == "000000":
        print("*Erro no KW* - O kw não pode possuir somente zeros")

    else:
        valida_custo(texto)


def valida_custo(texto):
    custo = texto[88:95]

    x = custo[0:5] + "." + custo[5:7]
    x = float(x)
    if x <= 0:
        print("*Erro no Custo* - O Custo não pode ser zero ou negativo")
    else:
        print("Tudo Okay")


def converte_numero(x):
    try:
        return int(x)
    except ValueError:
        print("O texto não contém apenas números")


def converte_decimal(x):
    try:
        return float(x)
    except ValueError:
        print("O texto não contém apenas números")


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


if __name__ == "__main__":
    tamanho = len(lista_texto)

    for i in lista_texto:
        valida_tamanho(i)
