from django.shortcuts import render
from django.utils import timezone
from .models import Guideline


def guideline_list(request):
    guideline = Guideline.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'datasheet/guideline_list.html', {'guideline': guideline})
