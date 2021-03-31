import re

texto_enel = "00000348340483300100051Bloco 1A apto 44    ##SSP29Março     20211544230007A16894030000840001550"
# print(len(texto_enel))

# print(texto_enel[10:18])

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
    regiao = texto[43:47]
    if regiao[0,1] != "##":
        print("*Erro na Região* - A Região não possui '##' como complemento")
    if regiao[2,4] != "SSP":
        print("*Erro na Região* - O Codigo da Região não é valido")
    else:
        valida_dia(texto)

def valida_dia(texto):
    dia = texto[48:49]
    if is_int(dia) == True:
       idia = converte_numero(dia)
    else:
        print("*Erro no Dia* - O dia não é um número")
    if idia == 0 or idia > 31:
        print("*Erro no Dia* - Esse dia não é valido")
    else:
        valida_mes(texto)

def valida_mes(texto):
    mes = texto[50:59]
    if month_okay(wicth_month(mes), mes) == False:
        print("*Erro no Mês* - Esse Mês não é valido")
    else:
        valida_ano(texto)

def valida_ano(texto):
    ano = texto[60:63]
    if ano == "0000":
        print("*Erro no Ano* - O ano não pode ser somento '0'")
    if is_int(ano) == False:
        print("*Erro no Ano* - O ano deve possuir somente números")
    if contains_special(ano) == True:
        print("*Erro no Ano* - O ano não pode possuir caracteres especiais")
    else:
        valida_hora(texto)

def valida_hora(texto):
    hora = converte_numero(texto[64:65])
    if hora > 23 or hora == 0:
        print("*Erro na Hora* - A Hora não é valida")
    else:
        valida_minuto(texto)

def valida_minuto(texto):
    minuto = converte_numero(texto[66:67])
    if minuto > 59:
        print("*Erro no Minuto* - O Minuto não é valido")
    if contains_special(minuto) == True:
        print("*Erro no Minuto* - O Minuto não pode Possuir um caractere especial")
    else:
        valida_segundo(texto)

def valida_segundo(texto):
    segundo = converte_numero(texto[68:69])
    if segundo > 59:
        print("*Erro no Segundo* - O Segundo não é valido")
    if contains_special(segundo) == True:
        print("*Erro no Segundo* - O Segundo não pode Possuir um caractere especial")
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
    aparelho = converte_numero(texto[80:81])
    if aparelho > 14 or aparelho <= 0:
        print("*Erro no Aparelho* - Esse Aparelho não é valido")
    else:
        valida_kw(texto)

def valida_kw(texto):
    kw = texto[82:87]
    if is_int(kw) == False:
        print("*Erro no KW* - O kw deve conter somente numeros")
    if kw == "000000":
        print("*Erro no KW* - O kw não pode possuir somente zeros")
    if contains_special(kw):
        print("*Erro no KW* - O kw não deve conter caracteres especiais")
    else:
        valida_custo(texto)

def valida_custo(texto):
    custo = converte_numero(texto[88:92] + "." + texto[92:94])
    if custo <= 0:
        print("*Erro no Custo* - O Custo não pode ser zero ou negativo")
    else:
        print("Tudo Okay")



def converte_numero(x):
    try:
        return int(x)
    except ValueError:
        print("O texto não contém apenas números")


def is_int(x):
    if type(x) == int:
        return True
    return False


def contains_special(texto):
    # Make own character set and pass
    # this as argument in compile method

    string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    # Pass the string in searchs
    # method of regex object.

    if(string_check.search(texto) == None):
        return False
    return True
def month_okay(n,mes):
    if n == 1:
        if mes[7,9] == "   ":
            return True
    elif n == 2:
        if mes[8,9] == " ":
            return True
    elif n == 3:
        if mes[5:9] == "     ":
            return True
    elif n == 4:
        if mes[5:9] == "     ":
            return True
    elif n == 5:
        if mes[4:9] == "      ":
            return True
    elif n == 6:
        if mes[5:9] == "     ":
            return True
    elif n == 7:
        if mes(5,9) == "     ":
            return True
    elif n == 8:
        if mes[6:9] == "    ":
            return True
    elif n == 9:
        if mes[8:9] == "  ":
            return True
    elif n == 10:
        if mes[7:9] == "   ":
            return True
    elif n == 11:
        if mes[8:9] == "  ":
            return True
    elif n == 12:
        if mes[8:9] == "  ":
            return True
    else:
        return False


def wicth_month(x):
    if x[0:6] == "Janeiro":
        return 1
    
    elif x[0:8]  == "Fevereiro":
        return 2
    
    elif x[0:4] == "Março":
        return 3
    
    elif x[0:4] == "Abril":
        return 4
    
    elif x[0:3] == "Maio":
        return 5
    
    elif x[0:4] == "Junho":
        return 6
    
    elif x[0:4] == "Julho":
        return 7
    
    elif x[0,5] == "Agosto":
        return 8
    
    elif x[0,7] == "Setembro":
        return 9
    
    elif x[0,6] == "Outubro":
        return 10
    
    elif x[0,7] == "Novembro":
        return 11
    
    elif x[0,7] == "Dezembro":
        return 12

    else:
        return 13








valida_tamanho(texto_enel)
