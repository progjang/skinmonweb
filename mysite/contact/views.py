# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings
#------- 함수로 구현한 contactForm 뷰
# def contact(request):
#     form = contactForm(request.POST or None)
#
#     if form.is_valid():
#         #print request.POST
#         #print form.cleaned_data['email']
#         name = form.cleaned_data['name']
#         comment = form.cleaned_data['comment']
#         subject = 'Message from MYSITE.com'
#         message = '%s\n\n from %s' %(comment, name)
#         emailFrom = form.cleaned_data['email']
#         emailTo = [settings.EMAIL_HOST_USER]
#         send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
#
#     context = locals()
#     template = 'contact/contact.html'
#     return render(request, template, context)
from django.views.generic.edit import FormView
from .forms import contactForm
#------- 클래스로 구현한 contactForm 뷰
class ContactFormView(FormView):
    form_class = contactForm
    template_name = 'contact/contact.html'

    def form_valid(self,form):
        name = self.request.POST['name']
        comment = self.request.POST['comment']
        subject = 'Message from MYSITE.com'
        message = '%s\n\n from %s' % (comment, name)
        emailFrom = self.request.POST['email']
        emailTo = [settings.EMAIL_HOST_USER]

        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)

        confirm_message = "Thanks for the message. We will get right back to you."

        context = {}
        #context['form'] = form
        context['sender'] = name
        context['email'] = emailFrom
        context['confirm_message'] = confirm_message
        return render(self.request, self.template_name, context)