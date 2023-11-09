from django.db import models

# Create your models here.     
class Proprietario(models.Model):
    nome             = models.CharField(max_length=100)
    email            = models.CharField(max_length=30)
    telefone         = models.CharField(max_length=15)
    data_cadastro    = models.DateTimeField(auto_now_add=True)
    cep              = models.CharField(max_length=8)
    logradouro       = models.CharField(max_length=255)
    bairro           = models.CharField(max_length=100)
    numero           = models.IntegerField()
    complemento      = models.CharField(max_length=40)
    uf               = models.CharField(max_length=40)
    municipio        = models.CharField(max_length=40)
    cpf              = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome
    
class Motos(models.Model):
    marca            = models.CharField(max_length=30)
    modelo           = models.CharField(max_length=30)
    cor              = models.CharField(max_length=30)
    ano              = models.IntegerField()
    proprietario_id  = models.ForeignKey(Proprietario, on_delete=models.CASCADE)
    placa            = models.CharField(max_length=8)
    data_cadastro    = models.DateTimeField(auto_now_add=True)
    kilometragem     = models.IntegerField()
    
    def __str__(self):
        return self.placa
    
class Agendamento(models.Model):
    data             = models.DateField()
    servicos         = models.CharField(max_length=255)
    proprietario_id  = models.ForeignKey(Proprietario, on_delete=models.CASCADE)
    moto_id          = models.ForeignKey(Motos, on_delete=models.CASCADE)
    status           = models.CharField(default="Aguardando aprovação", max_length=30)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    
    def __int__(self):
        return self.moto_id