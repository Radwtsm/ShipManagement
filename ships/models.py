from django.db import models


# Create your models here.

class Persona(models.Model):
    nome = models.CharField(max_length=255)
    cognome = models.CharField(max_length=255)
    indirizzo = models.CharField(max_length=255)
    contatto = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Persone"
    
    def __str__(self) -> str:
        return f"{self.nome} {self.cognome} / {self.contatto} / {self.indirizzo} "

class Nave(models.Model):
    num_registro = models.CharField(max_length=255,primary_key=True)
    nome = models.CharField(max_length=255)
    dimensioni = models.CharField(max_length=255)
    proprietario = models.ForeignKey(Persona,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Navi"
        
    def __str__(self) -> str:
        return f"{self.nome} / {self.num_registro} / {self.proprietario} / {self.dimensioni} "
         
    # proprietario
    # equipaggio

class Certificato(models.Model):
    codice = models.CharField(max_length=255,primary_key=True)
    nome = models.CharField(max_length=255)
    nave = models.ForeignKey(Nave,on_delete=models.CASCADE)
    data_scadenza = models.DateTimeField(blank=True,null=False)
    data_scadenza = models.DateTimeField(blank=True,null=False)
    scaduto = models.BooleanField(blank=False,null=False)
    class Meta:
        verbose_name_plural = "Certificati"
        
    def __str__(self) -> str:
        return f"{self.nome} {self.codice} / NAVE : {self.nave.num_registro}"

    
class Documento(models.Model):
    nave = models.ForeignKey(Nave,on_delete=models.CASCADE)
    file = models.FileField(upload_to ='documenti/')
    class Meta:
        verbose_name_plural = "Documenti" 
        
    def __str__(self) -> str:
        return f"doc nave:{self.nave.num_registro}" 
    
    
    
    # data_scadenza = models.DateTimeField(blank=True,null=False)
    # scaduto = models.BooleanField(blank=False,null=False)
    # description = models.CharField(max_length=2000)
    
