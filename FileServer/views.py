from django.shortcuts import render
from . import models
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
import os
from django.conf import settings


# Create your views here.
def get_all_file_types():
    return [detail.file_type for detail in models.File.objects.all()]

def get_all_file_details(file_type=None):
    return [str(detail.file).split('/')[-1] for detail in models.File.objects.all()]

def get_file_details():
    details = list()
    for other in list(zip(get_all_file_details(), get_all_file_types())):
        details.append({'file': other[0], 'file_type': other[1]})
    print(details)
    return {'file_types':set(get_all_file_types()), 'details':details}

def get_single_file_detail(request, file_type):
    single_file_details = list()
    files = [str(detail.file).split('/')[-1] for detail in models.File.objects.filter(file_type=file_type)]
    for file in files:
        single_file_details.append({'file':file, 'file_type':file_type})
    return JsonResponse({'single_file_details':single_file_details})

def main(request):
    return render(request, 'main.html', get_file_details())

def download_file(request, file_type, file_name):
    path = file_type +'/'+ file_name
    file_path = models.File.objects.filter(file=path)[0].file
    path = os.path.join(settings.MEDIA_ROOT, path)
    print('')
    response = HttpResponse(open(path, 'rb'), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename='+file_name
    return response
