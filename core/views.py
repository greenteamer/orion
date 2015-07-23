# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from core.models import Page, InfoBlock, Photo, Contacts
from django.core.mail import send_mail, EmailMultiAlternatives
from project.settings import ADMIN_EMAIL


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get(self, request):
        page = Page.objects.get(title=u'Главная')
        blocks = InfoBlock.objects.filter(page=page)[:3]
        images = Photo.objects.all()
        contacts = Contacts.objects.get(id=1)
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))

    def post(self, request):
        if 'phone' in request.POST:
            subject = u'заявка на orionsibir.ru от %s' % request.POST['name']
            message = u'Имя: %s \n телефон: %s' % (request.POST['name'], request.POST['phone'])
            send_mail(subject, message, 'teamer777@gmail.com', [ADMIN_EMAIL], fail_silently=False)
        return HttpResponseRedirect('/')
