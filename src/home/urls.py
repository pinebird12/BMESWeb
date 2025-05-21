from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('committees/<slug:committee>', views.committee_page)
]
