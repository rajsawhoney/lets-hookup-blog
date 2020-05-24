from django import template

register = template.Library()


@register.filter('slice')
def slice(arg, index):
    return arg[:index]


@register.filter(name='times')
def times(number):
    return range(number)
