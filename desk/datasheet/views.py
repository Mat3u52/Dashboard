import datetime

from django.shortcuts import render
from django.utils import timezone
from .models import Guideline


def guideline_list(request):
    current_date = datetime.date.today()
    guideline = Guideline.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'datasheet/guideline_list.html',
                  {'current_date': current_date,
                   'guideline': guideline})
