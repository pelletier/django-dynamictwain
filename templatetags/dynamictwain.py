from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('dynamictwain/widget.html')
def scan_widget(size="600x800", multiple=True):
    size = size.split('x')
    width = size[0]
    height = size[1]
    if multiple:
        multiple = 'true'
    else:
        multiple = 'false'
    data = {
        'base_url': getattr(settings,'DYNAMIC_TWAIN_MEDIA_ROOT',"/site_media/dynamic_twain/"),
        'width': width,
        'height': height,
        'multiple': multiple,
    }
    return data
