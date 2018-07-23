from django import template
from django.utils.safestring import  mark_safe


register = template.Library()  # register 是固定的变量名

@register.simple_tag
def my_add100(v1):
    return v1 + 100

@register.filter
def my_add1(v1,v2):
    return v1+v2+1