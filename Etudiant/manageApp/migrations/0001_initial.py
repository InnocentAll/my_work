# Generated by Django 4.1.5 on 2023-02-23 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(blank=True, max_length=20, unique=True)),
                ('email', models.CharField(max_length=250, unique=True)),
                ('quartier', models.CharField(max_length=200)),
                ('ville', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('credit', models.FloatField(blank=True, max_length=15)),
                ('note', models.FloatField(blank=True, max_length=15)),
                ('appreciation', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('naissance', models.DateTimeField(verbose_name='date de naissance')),
                ('genre', models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], max_length=32)),
                ('nationnalite', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='static/photo')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='manageApp.personne')),
                ('matricule', models.CharField(max_length=32)),
                ('grade', models.CharField(max_length=100)),
                ('poste', models.CharField(max_length=100)),
                ('type_poste', models.CharField(max_length=100)),
                ('adresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageApp.adresse')),
                ('matiere', models.ManyToManyField(to='manageApp.matiere')),
            ],
            bases=('manageApp.personne',),
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='manageApp.personne')),
                ('matricule', models.CharField(max_length=32, unique=True)),
                ('filiere', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Ancien', 'Ancien'), ('Nouveau', 'Nouveau')], max_length=32)),
                ('niveau', models.CharField(choices=[('L1', 'Licence 1'), ('L2', 'Licence 2'), ('L3', 'Licence 3')], max_length=32)),
                ('regime', models.CharField(choices=[('Special', 'Special'), ('Normal', 'Normal')], max_length=15)),
                ('Matiere', models.ManyToManyField(to='manageApp.matiere')),
                ('adresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageApp.adresse', unique=True)),
            ],
            bases=('manageApp.personne',),
        ),
    ]
