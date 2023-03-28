import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Guideline
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import GuideForm
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GuidelineSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Image(TemplateView):
    form = GuideForm
    template_name = 'datasheet/image.html'

    def guideline(self, request, *args, **kwargs):
        form = GuideForm(request.POST, request.FILES)
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
    # object_list = Guideline.publish_date.all()
    object_list = Guideline.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    # current_date = datetime.date.today()
    try:
        guideline = paginator.page(page)
    except PageNotAnInteger:
        guideline = paginator.page(1)
    except EmptyPage:
        guideline = paginator.page(paginator.num_pages)
    # guideline = Guideline.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')

    return render(request, 'datasheet/guideline_list.html',
                  #{'current_date': current_date,
                  {'guideline': guideline})


def guideline_detail(request, pk):
    # current_date = datetime.date.today()
    one_guideline = get_object_or_404(Guideline, pk=pk)
    return render(request, 'datasheet/guideline_detail.html', {'one_guideline': one_guideline})
                                                               # 'current_date': current_date})


def error_404_view(request, exception):
    data = {"name": 'Guideline for AXI.'}
    return render(request, 'datasheet/404.html', data)


def error_500_view(request, *args, **argv):
    return render(request, 'datasheet/500.html', status=500)


def guide_new(request):
    # current_date = datetime.date.today()
    if request.method == "POST":
        form = GuideForm(request.POST, request.FILES)
        if form.is_valid():
            guide = form.save(commit=False)
            guide.author = request.user
            guide.publish_date = timezone.now()
            guide.save()
            return redirect('guideline_detail', pk=guide.pk)
    else:
        form = GuideForm()

    return render(request, 'datasheet/guideline_edit.html', {'form': form})
                                                             # 'current_date': current_date})


def guideline_edit(request, pk):
    # current_date = datetime.date.today()
    guide = get_object_or_404(Guideline, pk=pk)
    if request.method == "POST":
        form = GuideForm(request.POST, request.FILES, instance=guide)
        if form.is_valid():
            guide = form.save(commit=False)
            guide.author = request.user
            guide.publish_date = timezone.now()
            guide.save()
            return redirect('guideline_detail', pk=guide.pk)
    else:
        form = GuideForm(instance=guide)

    return render(request, 'datasheet/guideline_edit.html', {'form': form})
                                                             #'current_date': current_date})


class GuideListView(ListView):  # Object solution. It is proceeding as first.
    queryset = Guideline.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    context_object_name = 'guideline'
    paginate_by = 3
    template_name = 'desk/datasheet/guideline_list.html'


class GuidelineViews(APIView):

    def post(self, request):
        serializer = GuidelineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk:
            item = Guideline.objects.get(id=pk)
            serializer = GuidelineSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Guideline.objects.all()
        serializer = GuidelineSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, pk=None):
        item = Guideline.objects.get(id=pk)
        serializer = GuidelineSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, pk=None):
        item = get_object_or_404(Guideline, id=pk)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


