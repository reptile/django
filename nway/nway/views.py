# Create your views here.
from django.shortcuts import render_to_response
#from django.template import Context, loader
#from django.http import HttpResponse

def home(request):
    #v = loader.get_template('index.html')
    #ctx = Context()
    #return HttpResponse(v.render(ctx))
    return render_to_response('index.html', {})
