* Dynamic Twain does not support uploading on a port other than 80.
* Firefox won't automatically install the extension if your host is represented
  by its IP address.
* Don't forget to change my hard-coded values.
* You need jQuery.


Basically
---------

    <form action="/foobar/" method="post" accept-charset="utf-8">
        
        <input type="text" name="some_name" value="">
        ... many other fields ...

        {% scan_widget "600x800" "False" %}

        {% submit_for_with_scan %}
    
    </form>


Turn False to True to enable multiple file upload.

In your view, the scanned file will be in request.FILES['pdf']



Settings.py
-----------

    import mimetypes

    mimetypes.add_type("Application/x-xpinstall", ".xpi", True)

    DYNAMIC_TWAIN_MEDIA_ROOT = "/site_media/dynamic_twain/"
    DYNAMIC_TWAIN_DEFAULT_RESOLUTION = 150
    DYNAMIC_TWAIN_SERVER = "mbp"

    #from django.core.urlresolvers import reverse

    #DYNAMIC_TWAIN_UPLOAD_PATH = reverse('twain:scan')

    DYNAMIC_TWAIN_UPLOAD_PATH = "/twain/upload/"

