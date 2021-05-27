from django.urls import path,re_path
from .import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('countries/', views.country_list),
    re_path('^countries/(?P<country>.+)/$', views.Country_List_Details.as_view())


]
urlpatterns = format_suffix_patterns(urlpatterns)