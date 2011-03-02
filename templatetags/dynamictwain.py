from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('dynamictwain/submit.html')
def submit_for_with_scan():
    return {}

@register.inclusion_tag('dynamictwain/widget.html')
def scan_widget(size="600x800", multiple=True):
    if multiple == "False":
        multiple = False
    elif multiple == "True":
        multiple = True
    size = size.split('x')
    width = size[0]
    height = size[1]
    if multiple:
        multiple = 'true'
    else:
        multiple = 'false'
    data = {
        'base_url': getattr(settings,'DYNAMIC_TWAIN_MEDIA_ROOT',"/site_media/dynamic_twain/"),
        'default_resolution': getattr(settings,'DYNAMIC_TWAIN_DEFAULT_RESOLUTION', 150),
        'server': getattr(settings, 'DYNAMIC_TWAIN_SERVER', 'localhost'),
        'upload_path': getattr(settings, 'DYNAMIC_TWAIN_UPLOAD_PATH', '/twain/upload/'),
        'width': width,
        'height': height,
        'multiple': multiple,
    }
    return data
