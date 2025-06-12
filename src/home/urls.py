from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('committees/<slug:committee>', views.committee_page),
    path('join-us', views.involvement, name='involvement'),
    path('tmd', views.mid, name='mid'),
    path('lexpo', views.lexpo, name='lexpo'),
    path('beday', views.beday, name='beday'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
