from django import template
from mailing.forms import ContactDataForm

register = template.Library()

@register.inclusion_tag('mailing/tags/form.html')
def contactdata_form():
    return {'contactdata_form': ContactDataForm()}