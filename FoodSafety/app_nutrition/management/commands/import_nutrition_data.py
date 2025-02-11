from django.core.management.base import BaseCommand
from app_nutrition.models import FoodNutrition
import pandas as pd

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # 读取Excel文件
        df = pd.read_excel('FoodNutrition.xls')
        for index, row in df.iterrows():
            FoodNutrition.objects.update_or_create(
                FoodName=row['食物(100g)'],
                Calorie=row['热能(Kcal)'],
                Protein=row['蛋白质(g)'],
                Fat=row['脂肪(g)'],
                Sugar=row['糖类(g)'],
                VA=row['VA(ug)'],
                VC=row['VC(mg)'],
                VB1=row['VB1(mg)'],
                VB2=row['VB2(mg)'],
                Ca=row['钙(mg)'],
                Fe=row['铁(mg)'],
                Zn=row['锌(mg)'],
                Water=row['水分(g)'],
                Cellulose=row['纤维素(g)'],
                Carotene=row['胡萝卜素(ug)'],
                Retinol=row['视黄醇(ug)'],
                VPP=row['维生素PP(mg)'],
                VE=row['维生素E(mg)'],
                Cholesterol=row['胆固醇(mg)'],
                K=row['钾(mg)'],
                Na=row['钠(mg)'],
                Mg=row['镁(mg)'],
                Mn=row['锰(mg)'],
                Cu=row['铜(mg)'],
                P=row['磷(mg)'],
                Se=row['硒(mg)']
            )



