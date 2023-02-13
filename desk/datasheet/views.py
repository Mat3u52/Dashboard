import datetime

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Guideline
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.forms import ModelForm
from .forms import ImgForm
from django.views.generic import DetailView
from django.views.generic import TemplateView


class Image(TemplateView):
    form = ImgForm
    template_name = 'datasheet/image.html'

    def guideline(self, request, *args, **kwargs):
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('image_display', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.guideline(request, *args, **kwargs)


class ImageDisplay(DetailView):
    model = Guideline
    template_name = 'datasheet/image_display.html'
    context_object_name = 'image'


def guideline_list(request):
    current_date = datetime.date.today()
    guideline = Guideline.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'datasheet/guideline_list.html',
                  {'current_date': current_date,
                   'guideline': guideline})


def guideline_detail(request, pk):
    one_guideline = get_object_or_404(Guideline, pk=pk)
    return render(request, 'datasheet/guideline_detail.html', {'one_guideline': one_guideline})


