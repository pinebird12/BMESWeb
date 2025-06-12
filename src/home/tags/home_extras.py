from django import template
from django.apps import apps

register = template.Library()

@register.simple_tag
def committees():
    Committee = apps.get_model('home', 'Committee')
    return Committee.objects.all()
