

from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.main, name='main'),
    path('get/<str:file_type>', view=views.get_single_file_detail, name='get_file_detail'),
    path('download/<str:file_type>/<str:file_name>', view=views.download_file, name='download_file')
]

