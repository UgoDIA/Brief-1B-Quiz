# Generated by Django 4.1.2 on 2022-11-17 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_quizz_nomfichier_alter_quizz_urlfichier'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='historique',
            unique_together={('matricule', 'idsession')},
        ),
    ]
