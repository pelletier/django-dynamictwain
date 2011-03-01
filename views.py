from django.shortcuts import render_to_response as render
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.http import HttpResponse


def scan(request):

    return render('dynamictwain/scan.html', {}, RequestContext(request))


@csrf_exempt
def upload(request):
    if not request.method == 'POST':
        pass # gofuckyourself

    # RemoteFile
    f = request.FILES['RemoteFile']
    destination = open('/tmp/%s' % f.name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    
    return HttpResponse()
