from django.http import HttpResponse
from django.shortcuts import render

fill = {"Желаемая должность": "Плотник", "Опыт работы": "5 лет",
        "Образование": "Среднее образование", "Курсы": "-",
        "Ключевые навыки": "Изготовление мебели", "Дополнительная информация": "Добросовестный"}

fill = fill.items()


# Create your views here.
def index(request):  # HttpRequest
    return render(request, "resume/Base.html", {"fill": fill, "name": "Иван Васильевич", "birthday": "12.02.84"})
