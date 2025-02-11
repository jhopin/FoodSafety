from django.core.management.base import BaseCommand
from app_nutrition.models import NutritionDisease
import pandas as pd

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # 读取Excel文件
        df1 =pd.read_excel('NutritionDisease.xlsx')
        for index, row in df1.iterrows():
            NutritionDisease.objects.update_or_create(
                DiseaseName=row['Disease'],
                VC=row['VC'],
                VE=row['VE'],
                VPP=row['VPP'],
                Cellulose=row['Cellulose'],
                Carotene=row['Carotene'],
                Zn=row['Zn'],
                Se=row['Se'],
                K=row['K'],
                Ca=row['Ca'],
                Mg=row['Mg'],
                Fe=row['Fe'],
                VB1=row['VB1'],
                VB2=row['VB2']
            )