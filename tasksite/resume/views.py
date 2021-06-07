from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):  # HttpRequest
    return render(request, "resume/Base.html", {"name": "Иван Васильевич", "birthday": "12.02.84", "job": "Плотник",
                                                "exp": "5 лет", "edu": "Среднее образование", "courses": "-",
                                                "skills": "Изготовление мебели", "add": "Добросовестный"})
