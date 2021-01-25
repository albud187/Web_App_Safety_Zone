from django.shortcuts import render

# Create your views here.
from django.core import mail
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.views.generic import TemplateView

class FlightSafetyReportView(TemplateView):
    template_name = 'app_reports/FlightSafetyReportForm.html'

class FlightSafetyReportConfirmView(TemplateView):
    template_name = 'app_reports/FlightSafetyReportConfirm.html'

def test(request):

    contact_email = request.GET['contact_email']
    contact_number= request.GET['contact_number']
    date_time = request.GET['date_time']
    description = request.GET['description']
    location = request.GET['location']
    print('testing')
    print(contact_email)
    print(contact_number)
    print(date_time)
    print(description)
    print(location)
    print('test complete')
    return render(request, 'app_reports/FlightSafetyReportConfirm.html')

def post_and_send(request):
    #saves data onto django database
    #sends email
    pass

def send_results(function_name,request,output_path):

    ## send email
    email_subject = 'flight safety report placeholder'
    email_text = 'please find enclosed results of '
    sender = ''
    recipient = [request.POST['user_recipient']]
    bcc =[]
    reply_to=[]
    headers={}
    email = EmailMessage(
        email_subject,
        email_text,
        sender,
        recipient,
        bcc,
        reply_to,
        headers
    )
    email.attach_file(output_path)
    email.send()
