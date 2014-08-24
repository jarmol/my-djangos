from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
import datetime

def index(request):
    a = "<li><a href='/hello'>browser data</a>"
    b = "<li><a href='/time'>UTC time now</a>"
    c = "<li><a href='/time/plus/3'>UTC +3 hours</a>"

    return HttpResponse('<ul>'+a+b+c+'</ul>')

def hello(request):
    message = "Your browser is %s and IP %s %s"
    ua = request.META['HTTP_USER_AGENT']
    ub = request.META['REMOTE_ADDR']
    uc = "<p><a href='/index/'>return_main</a>"
    return HttpResponse(message % (ua, ub, uc))

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    uc = "<p><a href='/index/'>return_main</a>"
    html = "<html><body>Local time %s UTC + %s h. %s</body></html>" % (dt, offset, uc)
    return HttpResponse(html)
