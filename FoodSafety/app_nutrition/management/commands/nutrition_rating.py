from django.core.management.base import BaseCommand
from app_nutrition.models import FoodNutritionRating
import pandas as pd

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # 读取Excel文件
        df = pd.read_excel('FoodNutrition.xls')
        max_values=df.max()
        for index, row in df.iterrows():
            FoodNutritionRating.objects.update_or_create(
                FoodName=row['食物(100g)'],
                Calorie=row['热能(Kcal)']/max_values['热能(Kcal)'],
                Protein=row['蛋白质(g)']/max_values['蛋白质(g)'],
                Fat=row['脂肪(g)']/max_values['脂肪(g)'],
                Sugar=row['糖类(g)']/max_values['糖类(g)'],
                VA=row['VA(ug)']/max_values['VA(ug)'],
                VC=row['VC(mg)']/max_values['VC(mg)'],
                VB1=row['VB1(mg)']/max_values['VB1(mg)'],
                VB2=row['VB2(mg)']/max_values['VB2(mg)'],
                Ca=row['钙(mg)']/max_values['钙(mg)'],
                Fe=row['铁(mg)']/max_values['铁(mg)'],
                Zn=row['锌(mg)']/max_values['锌(mg)'],
                Water=row['水分(g)']/max_values['水分(g)'],
                Cellulose=row['纤维素(g)']/max_values['纤维素(g)'],
                Carotene=row['胡萝卜素(ug)']/max_values['胡萝卜素(ug)'],
                Retinol=row['视黄醇(ug)']/max_values['视黄醇(ug)'],
                VPP=row['维生素PP(mg)']/max_values['维生素PP(mg)'],
                VE=row['维生素E(mg)']/max_values['维生素E(mg)'],
                Cholesterol=row['胆固醇(mg)']/max_values['胆固醇(mg)'],
                K=row['钾(mg)']/max_values['钾(mg)'],
                Na=row['钠(mg)']/max_values['钠(mg)'],
                Mg=row['镁(mg)']/max_values['镁(mg)'],
                Mn=row['锰(mg)']/max_values['锰(mg)'],
                Cu=row['铜(mg)']/max_values['铜(mg)'],
                P=row['磷(mg)']/max_values['磷(mg)'],
                Se=row['硒(mg)']/max_values['硒(mg)']
            )