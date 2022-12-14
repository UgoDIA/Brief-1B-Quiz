# Generated by Django 4.1.3 on 2022-11-03 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('matricule', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('idlogin', models.CharField(db_column='idLogin', max_length=30)),
                ('mdp', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'personnel',
            },
        ),
        migrations.CreateModel(
            name='Secteur',
            fields=[
                ('codesecteur', models.CharField(db_column='codeSecteur', max_length=10, primary_key=True, serialize=False)),
                ('nomsecteur', models.CharField(db_column='nomSecteur', max_length=20)),
            ],
            options={
                'db_table': 'secteur',
            },
        ),
        migrations.CreateModel(
            name='Collaborateur',
            fields=[
                ('matricule', models.OneToOneField(db_column='matricule', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='testdb.personnel')),
            ],
            options={
                'db_table': 'collaborateur',
            },
        ),
        migrations.CreateModel(
            name='Superuser',
            fields=[
                ('matricule', models.OneToOneField(db_column='matricule', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='testdb.personnel')),
            ],
            options={
                'db_table': 'superuser',
            },
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('idquizz', models.IntegerField(db_column='idQuizz', primary_key=True, serialize=False)),
                ('nomfichier', models.CharField(db_column='nomFichier', max_length=30)),
                ('urlfichier', models.CharField(db_column='urlFichier', max_length=200)),
                ('codesecteur', models.ForeignKey(db_column='codeSecteur', on_delete=django.db.models.deletion.DO_NOTHING, to='testdb.secteur')),
                ('matricule', models.ForeignKey(blank=True, db_column='matricule', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='testdb.superuser')),
            ],
            options={
                'db_table': 'quizz',
            },
        ),
        migrations.AddField(
            model_name='personnel',
            name='codesecteur',
            field=models.ForeignKey(db_column='codeSecteur', on_delete=django.db.models.deletion.DO_NOTHING, to='testdb.secteur'),
        ),
        migrations.CreateModel(
            name='Sessionquizz',
            fields=[
                ('idsession', models.IntegerField(db_column='idSession', primary_key=True, serialize=False)),
                ('evaluation', models.BooleanField()),
                ('datecreation', models.DateField(db_column='dateCreation')),
                ('dateexpiration', models.DateField(db_column='dateExpiration')),
                ('timer', models.TextField()),
                ('idquizz', models.ForeignKey(db_column='idQuizz', on_delete=django.db.models.deletion.DO_NOTHING, to='testdb.quizz')),
                ('matricule', models.ForeignKey(db_column='matricule', on_delete=django.db.models.deletion.DO_NOTHING, to='testdb.superuser')),
            ],
            options={
                'db_table': 'sessionQuizz',
            },
        ),
        migrations.CreateModel(
            name='Historique',
            fields=[
                ('matricule', models.OneToOneField(db_column='matricule', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='testdb.collaborateur')),
                ('score', models.SmallIntegerField(blank=True, null=True)),
                ('dateparticipation', models.DateField(blank=True, db_column='dateParticipation', null=True)),
                ('idsession', models.ForeignKey(db_column='idSession', on_delete=django.db.models.deletion.DO_NOTHING, to='testdb.sessionquizz')),
            ],
            options={
                'db_table': 'historique',
                'unique_together': {('matricule', 'idsession')},
            },
        ),
    ]
