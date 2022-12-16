from atexit import register
from django import template

register = template.Library()

@register.filter(name='remove_special')
def remove_chars(value, arg):
    for character in arg:
        print(character)
        value = value.replace(character,"")
    return value