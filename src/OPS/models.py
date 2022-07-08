from django.db import models

# Create your models here.

class Cellule(models.Model):
        code_cellule = models.CharField(max_length=50)
        libelle = models.CharField(max_length=50)
        # doit inclure la liste du personnel
        # doit inclure la liste des moyens sic


        def __init__(self):
            return self.code_cellule
               
# la table des aeronefs

class Aeronef(models.Model):
        immatriculation = models.CharField(max_length=20)
        type = models.CharField(max_length=30)
        heure_cellule = models.FloatField(max_length=10)
        landings = models.DecimalField(max_digits=10, decimal_places=10)
        cruise_speed = models.DecimalField(max_digits=10, decimal_places=10)
        libelle = models.CharField(max_length=20)
        serial_number = models.CharField(max_length=15)


        def __init__(self):
               return self.immatriculation

    
# les operations des organisees dans le CO

class Operations(models.Model):
        numero_ops = models.CharField(max_length=20)
        nom_ops = models.CharField(max_length=100)
        date_debut = models.DateField
        date_fin = models.DateField
        lieu = models.CharField(max_length=30)
        type = models.CharField(max_length=30)
        # inclure vehicule

        def __init__(self):
               return self.nom_ops

# les documents lies aux operations 

class Documents(models.Model):  # un document est lie a une operation
        type_doc = models.CharField(max_length=30, null=True)
        objet_doc = models.CharField(max_length =50)
        operation = models.ForeignKey('Operations', on_delete=models.CASCADE, null=True)


        def __init__(self):
               return self.type_doc


# les moyens utilises pendants les operations autres que les moyens roulants et avions

class moyens_sic(models.Model):
        nom_materiel = models.CharField(max_length=50)
        type_materiel = models.CharField(max_length=50)

        def __init__(self):
               return self.nom_materiel
# le personnel qui participents aux operations 

class Personnel(models.Model):
        grade_pers = models.CharField(max_length=20)
        nom_pers = models.CharField(max_length=30)
        prenom_pers = models.CharField(max_length=50)
        service = models.CharField(max_length=30)
        fonction = models.CharField(max_length=30)


        def __init__(self):
               return "%s %s"%(self.nom_pers, self.grade_pers)

# definition de la table mission - 
# Elle contiendra les missions effectuees de maniere quotidienne et des informations afferantes 

class Mission_Air(models.Model):
    libelle_mission = models.CharField(max_length=50)
    lieu_depart = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    pax = models.DecimalField(max_digits=5,decimal_places=2)
    heure_decollage = models.CharField(max_length=10)
    ETA = models.CharField(max_length=10)
    profit_de = models.CharField(max_length=50)
    statut = models.CharField(max_length=30)
    aeronef = models.OneToOneField(Aeronef, on_delete=models.CASCADE,null=True)
    #le personnel


    def __init__(self):
           return self.libelle_mission




class Vehicule(models.Model):
    panne = models.CharField(max_length=500)
    disponibilite = models.CharField(max_length=10)

    class Meta:
        abstract = True


class moto(models.Model):
        immatriculation_moto = models.CharField(max_length=20)
        libelle_moto = models.CharField(max_length=50)

        def __init__(self):
               return self.libelle_moto

class auto(models.Model):
        immatriculation_auto = models.CharField(max_length=20)
        libelle_auto = models.CharField(max_length=50)
        nombre_place = models.DecimalField(max_digits=10,decimal_places=2)
        type_auto = models.CharField(max_length=30)

        def __init__(self):
               return self.libelle_auto


class Mission_Terre(models.Model):
    libelle_mission = models.CharField(max_length=50)
    lieu_depart = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    pax = models.DecimalField(max_digits=5,decimal_places=2)
    heure_decollage = models.CharField(max_length=10)
    ETA = models.CharField(max_length=10)
    profit_de = models.CharField(max_length=50)
    statut = models.CharField(max_length=30)
    #doit etre lie a une auto
    #le personnel

    def __init__(self):
               return self.libelle_mission
