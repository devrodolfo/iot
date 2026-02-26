from django.db import models

# Create your models here.
class ReadSensors(models.Model):
    
    sensor_1 = models.FloatField()
    sensor_2 = models.FloatField()
    sensor_3 = models.FloatField()
    sensor_4 = models.FloatField()
    sensor_5 = models.FloatField()
    sensor_6 = models.FloatField()
    
    #no BD eu quero salvar o dia e a hora
    dia = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Leitura {self.id} - {self.dia} - {self.hora}"