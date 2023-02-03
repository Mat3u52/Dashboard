from django.shortcuts import render


def guideline_list(request):
    return render(request, 'datasheet/guideline_list.html', {})
