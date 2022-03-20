from django.conf import settings
from django.shortcuts import render,redirect
from django.core.mail import send_mail , BadHeaderError
from django.template import RequestContext
from django.template import loader
from datetime import datetime
from time import sleep


# Create your views here.

def contact(req):
    msgs=None
    if req.method == 'POST':
        subject = req.POST['subject']
        message = req.POST['message']
        contacter_email = req.POST['email']
        send_to =  'send_to@mail.com'
        email_from = settings.EMAIL_HOST_USER
        html_msg = loader.render_to_string(
            'email/contact_me_msg.html',
            {
                'client':contacter_email,
                'msg':message,
            }
        )
        try :
            send_mail( subject, message, email_from, [send_to,] ,fail_silently=False, html_message=html_msg)
            #starttime= datetime.now().second
            msgs = 'email is Sended successfuly !!'
            return redirect('contact')
            
        except BadHeaderError :
            msgs = 'Sorry, Something  wrong !!'

    return render(req,'pages/contact.html', {'msgs':msgs})
    #context_instance= RequestContext(req)