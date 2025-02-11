from django.shortcuts import render,HttpResponse
from app_nutrition.models import *
import pandas as pd

# Create your views here.
def DataGet(request):
    file="FoodNutrition.xls"
    df = pd.read_excel(file)
    return HttpResponse(df)


def DiseaseList(request):
    # 获取所有的疾病名称
    diseases = NutritionDisease.objects.all().values_list('DiseaseName')
    # 传递疾病名称列表到模板
    return render(request, 'Disease_list.html', {'diseases': diseases})

def Recommendation(request, DiseaseName):
    # 获取特定疾病的营养需求
    disease = NutritionDisease.objects.get(DiseaseName=DiseaseName)

    foods = FoodNutritionRating.objects.all()
    scored_foods = []
    for food in foods:
        score = (food.VC / (disease.VC or 1) if disease.VE > 0 else 0) + \
                (food.VE / (disease.VE or 1) if disease.VE > 0 else 0) + \
                (food.VPP / (disease.VPP or 1) if disease.VPP > 0 else 0) + \
                (food.Cellulose / (disease.Cellulose or 1) if disease.Cellulose > 0 else 0) + \
                (food.Carotene / (disease.Carotene or 1) if disease.Carotene > 0 else 0) + \
                (food.Zn / (disease.Zn or 1) if disease.Zn > 0 else 0) + \
                (food.Se / (disease.Se or 1) if disease.Se > 0 else 0) + \
                (food.K / (disease.K or 1) if disease.K > 0 else 0) + \
                (food.Ca / (disease.Ca or 1) if disease.Ca > 0 else 0) + \
                (food.Mg / (disease.Mg or 1) if disease.Mg > 0 else 0) + \
                (food.Fe / (disease.Fe or 1) if disease.Fe > 0 else 0) + \
                (food.VB1 / (disease.VB1 or 1) if disease.VB1 > 0 else 0) + \
                (food.VB2 / (disease.VB2 or 1) if disease.VB2 > 0 else 0)
        scored_foods.append((food, score))

    # 按评分排序并选取前3名
    scored_foods.sort(key=lambda x: x[1], reverse=True)
    top_10_foods = scored_foods[:10]

    # 传递到模板
    return render(request, 'Recommendation.html', {'top_10_foods': top_10_foods})






