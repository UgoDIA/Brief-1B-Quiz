# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Personnel(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    prenom = models.CharField(max_length=20)
    nom = models.CharField(max_length=20)
    matricule = models.CharField(primary_key=True, max_length=20)
    codesecteur = models.ForeignKey('Secteur', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Personnel'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Collaborateur(models.Model):
    matricule = models.OneToOneField(Personnel, models.DO_NOTHING, db_column='matricule', primary_key=True)

    class Meta:
        managed = False
        db_table = 'collaborateur'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(Personnel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Historique(models.Model):
    idhisto = models.AutoField(db_column='idHisto', primary_key=True)  # Field name made lowercase.
    score = models.IntegerField(blank=True, null=True)
    dateparticipation = models.DateField(db_column='dateParticipation', blank=True, null=True)  # Field name made lowercase.
    idsession = models.ForeignKey('Sessionquizz', models.DO_NOTHING, db_column='idSession')  # Field name made lowercase.
    matricule = models.ForeignKey(Collaborateur, models.DO_NOTHING, db_column='matricule')

    class Meta:
        managed = False
        db_table = 'historique'


class Quizz(models.Model):
    idquizz = models.AutoField(db_column='idQuizz', primary_key=True)  # Field name made lowercase.
    nomfichier = models.CharField(db_column='nomFichier', max_length=30)  # Field name made lowercase.
    urlfichier = models.CharField(db_column='urlFichier', max_length=200)  # Field name made lowercase.
    codesecteur = models.ForeignKey('Secteur', models.DO_NOTHING, db_column='codesecteur', blank=True, null=True)
    matricule = models.ForeignKey('Superuser', models.DO_NOTHING, db_column='matricule', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quizz'


class Secteur(models.Model):
    codesecteur = models.CharField(primary_key=True, max_length=10)
    nomsecteur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'secteur'


class Sessionquizz(models.Model):
    idsession = models.AutoField(db_column='idSession', primary_key=True)  # Field name made lowercase.
    evaluation = models.BooleanField()
    datecreation = models.DateField(db_column='dateCreation')  # Field name made lowercase.
    dateexpiration = models.DateField(db_column='dateExpiration', blank=True, null=True)  # Field name made lowercase.
    timer = models.IntegerField(blank=True, null=True)
    idquizz = models.ForeignKey(Quizz, models.DO_NOTHING, db_column='idQuizz')  # Field name made lowercase.
    matricule = models.ForeignKey('Superuser', models.DO_NOTHING, db_column='matricule')

    class Meta:
        managed = False
        db_table = 'sessionQuizz'


class Superuser(models.Model):
    matricule = models.OneToOneField(Personnel, models.DO_NOTHING, db_column='matricule', primary_key=True)
    role = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'superuser'
