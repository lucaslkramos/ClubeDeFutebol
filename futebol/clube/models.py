from django.db import models


class Tecnico(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome


class Patrocinador(models.Model):
    nome = models.CharField(max_length=100)
    valor_contrato = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Time(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)
    fundacao = models.IntegerField()
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    tecnico = models.ForeignKey(
        Tecnico,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    patrocinadores = models.ManyToManyField(
        Patrocinador,
        blank=True
    )

    def __str__(self):
        return self.nome