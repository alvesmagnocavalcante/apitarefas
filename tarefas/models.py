from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    tarefa = models.CharField(max_length=255)