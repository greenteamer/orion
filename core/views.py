# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext
from django.views.generic.base import TemplateView
from core.models import Page, InfoBlock, Photo


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get(self, request):

        page = Page.objects.get(title=u'Главная')
        blocks = InfoBlock.objects.filter(page=page)[:3]
        images = Photo.objects.all()
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))
