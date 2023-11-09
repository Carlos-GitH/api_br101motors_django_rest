import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from api_br101motors.models import *

def criando_proprietarios(quantidade):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade):
        nome=fake.name(),
        cpf=CPF().generate(),
        email=fake.email(),
        telefone= "{} 9{}-{}".format(random.randrange(10,99), random.randrange(4000, 9999), random.randrange(4000, 9999)),
        logradouro=fake.street_address(),
        bairro=fake.city(),
        uf=fake.state_abbr(),
        municipio=fake.city(),
        cep=fake.postcode(),
        complemento=fake.street_name(),
        p = Proprietario(nome=nome, cpf=cpf, email=email, telefone=telefone, logradouro=logradouro, bairro=bairro, uf=uf, municipio=municipio, cep=cep, numero=10, complemento=complemento)
        p.save()

criando_proprietarios(5)
print("sucesso")
