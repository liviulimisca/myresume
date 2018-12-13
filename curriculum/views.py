from django.shortcuts import render
from curriculum.models import Experience

def resume(request):
    all_experiences = Experience.objects.order_by("-id")
    context = {
    'all experiences': all_experiences,
    }

    return render(request, 'base.html', context)
