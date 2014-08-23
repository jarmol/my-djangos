from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
import datetime

def hello(request):
    message = "Your browser is %s and IP %s"
    ua = request.META['HTTP_USER_AGENT']
    ub = request.META['REMOTE_ADDR']
    return HttpResponse(message % (ua, ub))

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
    html = "<html><body>Local time %s UTC + %s h.</body></html>" % (dt, offset)
    return HttpResponse(html)
