from django.contrib import admin
from ships.models import Nave,Persona,Certificato,Documento

# Register your models here.
class NaveAdmin(admin.ModelAdmin):
    search_fields = ['num_registro', 'nome', 'dimensioni', 'proprietario__nome']

class PersonaAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'cognome', 'indirizzo', 'contatto']

class CertificatoAdmin(admin.ModelAdmin):
    search_fields = ['codice', 'nome', 'nave__num_registro']

class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ['nave__num_registro']



admin.site.register(Nave,NaveAdmin)
admin.site.register(Persona,PersonaAdmin)
admin.site.register(Certificato,CertificatoAdmin)
admin.site.register(Documento,DocumentoAdmin)
