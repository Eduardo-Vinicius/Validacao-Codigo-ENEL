
import jiphy


x = jiphy.to.python("function returnCep(line) {const cep = line.substr(10, 8); if (cep.length === 8 && isNumber(cep)) { return console.log(CEP: ${cep}); } else { throw 'Desculpe o CEP não passou na validação'; } }")

print(x)




def returnCep(line):
    cep = line.substr(10, 8)
    if cep.length is 8:
        return (cep)
    else:
        raise 'Desculpe o CEP não passou na validação'

returnCep(3928292)
