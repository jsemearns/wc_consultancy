from django.shortcuts import render
from django.views.generic import TemplateView


class UniversityTemplateView(TemplateView):
    template_name = 'universities/university.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UniversityTemplateView, self).get_context_data(
                        *args, **kwargs)
        print context
        return context
