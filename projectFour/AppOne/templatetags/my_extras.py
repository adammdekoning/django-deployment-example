from django import template

register = template.Library()

def cuz(value, arg):
    """
        This cuts out all values of "arg" from the string
    """

    return value.replace(arg,'')

register.filter('cuz', cuz)
