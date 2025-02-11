from django.db import models


class FoodNutrition(models.Model):
    FoodName = models.CharField(max_length=100)
    Calorie = models.IntegerField() #热量
    Protein = models.DecimalField(max_digits=10, decimal_places=2)
    Fat = models.DecimalField(max_digits=10, decimal_places=2)
    Sugar = models.DecimalField(max_digits=10, decimal_places=2)
    VA = models.DecimalField(max_digits=10, decimal_places=2)
    VC = models.DecimalField(max_digits=10, decimal_places=2)
    VB1 = models.DecimalField(max_digits=10, decimal_places=2)
    VB2 = models.DecimalField(max_digits=10, decimal_places=2)
    Ca = models.IntegerField()
    Fe = models.DecimalField(max_digits=10, decimal_places=2)
    Zn = models.DecimalField(max_digits=10, decimal_places=2)
    Water = models.DecimalField(max_digits=10, decimal_places=2)
    Cellulose = models.DecimalField(max_digits=10, decimal_places=2) #纤维素
    Carotene = models.IntegerField() #胡萝卜素
    Retinol = models.IntegerField() #视黄醇
    VPP = models.DecimalField(max_digits=10, decimal_places=2) #维生素PP
    VE = models.DecimalField(max_digits=10, decimal_places=2)
    Cholesterol = models.IntegerField() #胆固醇
    K = models.IntegerField()
    Na = models.DecimalField(max_digits=10, decimal_places=2)
    Mg = models.IntegerField()
    Mn = models.DecimalField(max_digits=10, decimal_places=2)
    Cu = models.DecimalField(max_digits=10, decimal_places=2)
    P = models.IntegerField()
    Se = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.FoodName

class FoodNutritionRating(models.Model):
    FoodName = models.CharField(max_length=100)
    Calorie = models.DecimalField(max_digits=10, decimal_places=2) #热量
    Protein = models.DecimalField(max_digits=10, decimal_places=2)
    Fat = models.DecimalField(max_digits=10, decimal_places=2)
    Sugar = models.DecimalField(max_digits=10, decimal_places=2)
    VA = models.DecimalField(max_digits=10, decimal_places=2)
    VC = models.DecimalField(max_digits=10, decimal_places=2)
    VB1 = models.DecimalField(max_digits=10, decimal_places=2)
    VB2 = models.DecimalField(max_digits=10, decimal_places=2)
    Ca = models.DecimalField(max_digits=10, decimal_places=2)
    Fe = models.DecimalField(max_digits=10, decimal_places=2)
    Zn = models.DecimalField(max_digits=10, decimal_places=2)
    Water = models.DecimalField(max_digits=10, decimal_places=2)
    Cellulose = models.DecimalField(max_digits=10, decimal_places=2) #纤维素
    Carotene = models.DecimalField(max_digits=10, decimal_places=2) #胡萝卜素
    Retinol = models.DecimalField(max_digits=10, decimal_places=2) #视黄醇
    VPP = models.DecimalField(max_digits=10, decimal_places=2) #维生素PP
    VE = models.DecimalField(max_digits=10, decimal_places=2)
    Cholesterol = models.DecimalField(max_digits=10, decimal_places=2) #胆固醇
    K = models.DecimalField(max_digits=10, decimal_places=2)
    Na = models.DecimalField(max_digits=10, decimal_places=2)
    Mg = models.DecimalField(max_digits=10, decimal_places=2)
    Mn = models.DecimalField(max_digits=10, decimal_places=2)
    Cu = models.DecimalField(max_digits=10, decimal_places=2)
    P = models.DecimalField(max_digits=10, decimal_places=2)
    Se = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.FoodName

class NutritionDisease(models.Model):
    DiseaseName=models.CharField(max_length=100)
    VC = models.IntegerField()
    VE = models.IntegerField()
    VPP = models.IntegerField()
    Cellulose = models.IntegerField()
    Carotene = models.IntegerField()
    Zn = models.IntegerField()
    Se = models.IntegerField()
    K = models.IntegerField()
    Ca = models.IntegerField()
    Mg = models.IntegerField()
    Fe = models.IntegerField()
    VB1 = models.IntegerField()
    VB2 = models.IntegerField()

    def __str__(self):
        return self.DiseaseName

