Django-Dynamictwain
===================

A reusable Django application for an almost painless integration of Dynamic Web
Twain in your project.

The idea (how it works)
-----------------------

It provides two template tags and some views so that you can easily either scan
some doc and send the results to your views, or integrates dynamictwain in your
existing forms.

The raw widget will just allow your user to scan a document then send the result
on your view.

The form integration is more sophisticated, because it will play ping-pong with
your Django server so that you receive the form payload plus the scanned file
directly in your view.

Some (quite important) notes
----------------------------

* Dynamic Twain does not support uploading on a port other than 80. Which means
  that you cannot run your development server on 8000 but on 80, so you need
  a root access to your computer.
* Firefox won't automatically install the extension if your host is represented
  by its IP address (tweak your `/etc/hosts` for testing).
* Some hard-coded values may remain in this app code.
* You need jQuery.

Installation
------------

1. Add `dynamictwain` to your `INSTALLED_APPS`.
2. Add the templates in `TEMPLATE_DIRS`.
3. Add `(r'^twain/', include('dynamictwain.urls', 'dynamictwain')),` in your
   `urls.py`.
4. `syncdb`.

You may consider taking a look at the "settings.py" section of this readme.

Basic raw integration
---------------------

    {% load dynamictwain %}
    {% scan_widget "600x800" "False" %}
    {% upload_scan %}
    

Turn `False` to `True` to enable multiple file upload. This will show additional
buttons for navigation between images.

In your view, the scanned file will be in request.FILES['pdf']

Basic form integration
----------------------

    {% load dynamictwain %}

    <form action="/foobar/" method="post" accept-charset="utf-8">
        
        <input type="text" name="some_name" value="">
        ... many other fields ...

        {% scan_widget "600x800" "False" %}

        {% submit_form_with_scan %}
    
    </form>

Concerning the scan widget
--------------------------

Example:

    {% scan_widget "600x800" "False" %}

The first argument is the size of the applet on the page, using the format
"(width)x(height)".

The second one is a boolean which enables multiple scans.

Have a glance at your settings.py
---------------------------------

`DYNAMIC_TWAIN_MEDIA_ROOT`: The base URL where the DynamicWebTwain plugins live.

    DYNAMIC_TWAIN_MEDIA_ROOT = "/site_media/dynamic_twain/"

`DYNAMIC_TWAIN_DEFAULT_RESOLUTION`: Default resolution in DPI for the scan. 150
is nice for web applications because it generates medium-sized files.

    DYNAMIC_TWAIN_DEFAULT_RESOLUTION = 150

`DYNAMIC_TWAIN_SERVER`: The web server name of the upload view. For example, if
your `include('dynamictwain')` points to `http://mysite.com/twain/`, you should
set `mysite.com` here.

    DYNAMIC_TWAIN_SERVER = "mysite.com"

`DYNAMIC_TWAIN_UPLOAD_PATH`: Consider the case above. This settings will be set
`/twain/upload/`.

    DYNAMIC_TWAIN_UPLOAD_PATH = "/twain/upload/"

