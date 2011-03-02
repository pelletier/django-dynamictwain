import json, re
from django.shortcuts import render_to_response as render
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.http import HttpResponse
from django.core.urlresolvers import resolve

from dynamictwain.models import TempFormData


def scan(request):

    return render('dynamictwain/scan.html', {}, RequestContext(request))


@csrf_exempt
def upload(request):
    if not request.method == 'POST':
        pass # gofuckyourself


    # RemoteFile

    print "hello"
    f = request.FILES['RemoteFile']
    print f
    print "foo"

    # Extract the ID.

    print f.name
    print re.match('.*\[(.+)\].*', f.name).group(1)
    uid = re.match('.*\[(.+)\].*', f.name).group(1)
    print "uid"
    print uid
    real_filename = f.name.replace("[%s]" % uid, '')
    print "real"
    print real_filename

    # Grab the temp data
    tmp = TempFormData.objects.get(pk=uid)
    tmp.scan = f
    tmp.save()
    
    #destination = open('/tmp/%s' % f.name, 'wb+')
    #for chunk in f.chunks():
        #destination.write(chunk)
    #destination.close()
    
    return HttpResponse()


@csrf_exempt
def form(request):
    # Convert to JSON for storage
    get = json.dumps(request.GET)
    post = json.dumps(request.POST)
    # Create a temporary object for storing request data
    tmp = TempFormData(orig_url=request.GET['orig'],json_get=get, json_post=post)
    tmp.save()

    uid = tmp.pk

    response = json.dumps({'uid':uid})

    return HttpResponse(response, mimetype='application/json')


@csrf_exempt
def redirect(request):
    uid = request.GET['uid']
    data = TempFormData.objects.get(pk=uid)

    print data.json_post
    print data.json_get

    #new_request = request.copy()
    new_request = request
    
    post = new_request.POST.copy()
    post.update(json.loads(data.json_post))
    new_request.POST = post
    
    get = new_request.GET.copy()
    get.update(json.loads(data.json_get))
    new_request.GET = get

    files = new_request.FILES.copy()
    files['pdf'] = data.scan
    new_request._files = files


    final_view = resolve(data.orig_url)[0]
    return final_view(new_request)
