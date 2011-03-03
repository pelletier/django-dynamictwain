from django.http import HttpResponse

# Create your views here.
def foo(request):
    val = request.GET['some_name']
    f = request.FILES
    return HttpResponse('Received value: %s. With file: %s' % (val,f))



def scan(request):
    return render('scan.html', {}, RequestContext(request))

