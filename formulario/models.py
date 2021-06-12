from django.db import models

# Create your models here.

class Deporte(models.Model):
    idDeporte = models.IntegerField(primary_key=True,verbose_name='Id de Deporte')
    nombreDeporte = models.CharField(max_length=50,verbose_name='Nombre del Deporte')
    def __str__(self):
        return self.nombreDeporte

class Evento(models.Model):
    idEvento = models.IntegerField(primary_key=True,verbose_name='Id de Evento')
    nombreEvento = models.CharField(max_length=50,verbose_name='Nombre del Evento')
    fechaEvento = models.CharField(max_length=50,verbose_name='Fecha del Evento')
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreEvento

class Cliente(models.Model):

    runCliente = models.CharField(max_length=9,primary_key=True, verbose_name='Run')
    nombreCliente = models.CharField(max_length=20, verbose_name='Nombre')
    apellidoPaterno = models.CharField(max_length=20,null=True, blank=True, verbose_name='Apellido Paterno')
    apellidoMaterno = models.CharField(max_length=20,null=True, blank=True, verbose_name='Apellido Materno')
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s' % (self.nombreCliente, self.apellidoPaterno, self.apellidoMaterno)



