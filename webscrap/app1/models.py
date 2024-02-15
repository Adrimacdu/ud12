from django.db import models

# Create your models here.

#UD12.1.a
class Criptodivisa(models.Model):

    nombre = models.CharField(max_length=20)
    fecha = models.DateField()
    precio = models.FloatField()


    def get_precio_formateado(self):
        if self.precio > 0:
            return "{:.2f}".format(self.precio)  # {}   marcador de posicion
        else:                                    # :    indica que a continuacion se especifica el formato
            return str(self.precio)              # .2   se deben mostrar dos digitos despues del punto de los decimales
                                                 # f    nos indica que es un float