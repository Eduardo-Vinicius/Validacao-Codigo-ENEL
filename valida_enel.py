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
        pass


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


valida_tamanho(texto_enel)
