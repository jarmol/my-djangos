#import django.shortcuts
from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello Python-Django world !")

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    #Ei toiminut shortcut renderin avulla
    #html = render(request, 'current_datetime.html', {'current_date': now})
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>Local time %s UTC + %s h.</body></html>" % (dt, offset)
    return HttpResponse(html)
