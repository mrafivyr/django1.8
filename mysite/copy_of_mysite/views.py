from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, get_connection
import datetime


def hello(request):
    return HttpResponse('Hello world')


def current_datetime(request):
    now = datetime.datetime.now()

    # Using Template and Context
    # t = Template('<html><body>Now the time is {{ now }}</body></html>')
    # t.render(Context({'now' : now}))

    # Using get_template from loader module
    # t = get_template('template.html')
    #
    # html = t.render({'person_name': 'Rafi Mohammed', 'company': 'Outdoor Equipment',
    #                          'ship_date': datetime.date(2017, 7, 2), 'ordered_warranty': False,
    #                          'item_list': ['Moto g5s plus', 'honor 7X']})

    # html = f'<html><body>Now the time is {now}</body></html>'

    # Using direct render method from shortcuts

    html = render(request, 'template_child.html', context={'person_name': 'Rafi Mohammed', 'company': 'Outdoor Equipment',
                                             'ship_date': datetime.date(2017, 7, 2), 'ordered_warranty': False,
                                             'item_list': ['Moto g5s plus', 'honor 7X']})
    return html


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    # assert False

    now = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = f'<html><body>In {offset} hour(s) time will be {now}</body></html>'
    # html = Template("<p>Thanks for placing an order from {{ company }}. "
    #                 "It's scheduled to ship on {{ now|date:'F j, Y'}}</p>")
    #
    # html.render(Context({'company': 'Wipro', 'now': now}))

    return HttpResponse(html)


def display_meta(request):
    values = request.META
    html = []
    for k in sorted(values):
        html.append(f'<tr><td>{k}</td><td>{values[k]}</td></tr>')

    html.append(f'<tr><td>{"#" * 20}</td><td>{"#" * 20}</td></tr>')

    html.append('<tr><td>"Details of GET request"</td></tr>')

    for key, val in request.GET.items():
        html.append(f'<tr><td>{key}</td><td>{val}</td></tr>')

    html.append(f'<tr><td>{"#" * 20}</td><td>{"#" * 20}</td></tr>')

    html.append('<tr><td>"Details of POST request"</td></tr>')

    for key, val in request.POST.items():
        html.append(f'<tr><td>{key}</td><td>{val}</td></tr>')

    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(cd['subject'],
                      cd['message'],
                      cd.get('email', 'noreply@example.com'),
                      ['siteowner@example.com'],
                      connection=con)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})

    return render(request, 'contact_form.html', {'form': form})


def message(request):
    return HttpResponse('Thanks for contacting us. Your request will acknowledged at the earliest')

