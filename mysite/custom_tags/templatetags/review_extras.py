from django import template


register = template.Library()


def cut(value, arg):
    return value.replace(arg, '')


@register.filter(name='mmm')
def lower(value):
    return value.lower()
