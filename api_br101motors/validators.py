import re
from validate_docbr import CPF

def cpf_valido(self, cpf):
    cpf_valid=CPF()
    return cpf_valid.validate(cpf)

def validate_nome(self, nome):
    return nome.isalpha()

def validate_telefone(telefone):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, telefone)
    return resposta