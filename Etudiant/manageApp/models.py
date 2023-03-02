from django.db import models

class Personne(models.Model):
    Genre = (
        ('Masculin',('Masculin')),
        ('Feminin',('Feminin')),
    )
    nom = models.CharField(max_length = 200)
    naissance = models.DateTimeField('date de naissance')
    genre = models.CharField(max_length = 32, choices = Genre)
    nationnalite = models.CharField(max_length = 50)
    photo = models.ImageField(upload_to='static/photo', blank=True)

    def __str__(self):
        return self.nom

class Adresse(models.Model):
    telephone = models.CharField(max_length = 20, blank = True, unique = True)
    email = models.CharField(max_length = 250, unique = True)
    quartier = models.CharField(max_length = 200)
    ville = models.CharField(max_length = 200)

    def __str__(self):
        return self.email

class Matiere(models.Model):
    nom = models.CharField(max_length = 150)
    credit = models.FloatField(max_length = 15, blank = True)
    note = models.FloatField(max_length = 15, blank = True)
    appreciation = models.CharField(max_length = 150)

    def __str__(self):
        return self.nom

class Etudiant(Personne):
    Status = (
        ('Ancien', ('Ancien')),
        ('Nouveau', ('Nouveau')),
    )
    Niveau = (
        ('L1', ('Licence 1')),
        ('L2', ('Licence 2')),
        ('L3', ('Licence 3')),
    )
    Regime = (
        ('Special', ('Special')),
        ('Normal', ('Normal')),
    )
    matricule = models.CharField(max_length = 32, unique=True)
    filiere = models.CharField(max_length = 100)
    status = models.CharField(max_length = 32, choices = Status)
    niveau = models.CharField(max_length = 32, choices = Niveau)
    regime = models.CharField(max_length = 15, choices = Regime)
    adresse = models.ForeignKey(Adresse, on_delete = models.CASCADE, unique=True)
    Matiere = models.ManyToManyField(Matiere)

    def __str__(self):
        return self.matricule

class Personnel(Personne):
    matricule = models.CharField(max_length = 32)
    grade = models.CharField(max_length = 100)
    poste = models.CharField(max_length = 100)
    type_poste = models.CharField(max_length = 100)
    adresse = models.ForeignKey(Adresse, on_delete = models.CASCADE)
    matiere = models.ManyToManyField(Matiere)

    def __str__(self):
        return self.matricule
