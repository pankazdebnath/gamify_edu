from django.shortcuts import render
from core.models import Grade


def index(request):
    grades = Grade.objects.all()
    context = {'grades': grades}
    if not grades.exists():
        context['message'] = 'There are currently no grades in the database.'  # Example message

    return render(request, 'core/index.html', context)
