from django.http import HttpResponse

# Create your views here.
def foo(request):
    print "Welcome to the foo view"
    print "\tVALUE %s" % request.GET['some_name']
    print "\tFILES %s" % request.FILES
    return HttpResponse('End.')
