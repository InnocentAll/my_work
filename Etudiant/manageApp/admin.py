from django.contrib import admin
from .models import*

# Register your models here.
#admin.site.register(Courses)

@admin.register(Etudiant)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom', 'genre', 'status',)
    ordering = ('matricule',)
    search_fields = ('matricule',)

@admin.register(Personnel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom', 'genre', 'grade',)
    ordering = ('matricule',)
    search_fields = ('matricule',)

@admin.register(Adresse)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('telephone', 'email', 'quartier', 'ville',)
    ordering = ('email',)
    search_fields = ('email',)

@admin.register(Matiere)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'credit','note', 'appreciation', )
    ordering = ('nom', )
    search_fields = ('nom', )
