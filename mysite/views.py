from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
#from django.shortcuts import render_to_response (anterior a render)
import datetime
from mysite.forms import ContactForm
from django.core.mail import send_mail
 
#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = get_template('dateapp/current_datetime.html')
    #html = "<html><body>It is now %s.</body></html>" % now
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request,'dateapp/current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()    
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template('dateapp/hours_ahead.html')
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    html = t.render(Context({'num_hours': offset, 'new_date': dt}))
    return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #send_mail(cd['subject'], cd['message'], cd.get('email', 'noreply@example.com'),['jezulonrs@gmail.com'], )
            
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})

    return render(request, 'contact_form.html', {'form':form})
