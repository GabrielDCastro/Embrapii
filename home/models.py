from django.db import models

class Cliente(models.Model):


    Nome_do_cliente = models.CharField(max_length=100)

    def __str__(self):

       return self.Nome_do_cliente


    Nascimento=models.DateField()

    TipoDeTeste = (

           ("RT-PCR","RT-PCR"),

           ("Sorologia", "Sorologia"),

           ("TAntigenos", "Teste Rápido - Antígenos"),

           ("TAnticorpos", "Teste Rápido - Anticorpos"),

           )
    Tipo_de_Teste_realizado = models.CharField(max_length=50, choices=TipoDeTeste)

    ResultadodoTeste =(
        ("P", "Positivo"),

        ("N", "Negativo")
    )
    Resultado_do_Teste = models.CharField(max_length=50, choices=ResultadodoTeste)
