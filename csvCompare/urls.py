from django.conf.urls import url
from . import views


app_name = 'csvCompare'

urlpatterns = [
url(r'^$', views.compare, name='index'),
url(r'^upload/$',views.upload_file_view,name='upload'),




]

