# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get(self, request):
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))
