from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from main.models import (University, Admission, Requirement)

UNIVERSITIES_PER_PAGE = 6


class UniversityTemplateView(TemplateView):
    template_name = 'universities/university_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UniversityTemplateView, self).get_context_data(
                        *args, **kwargs)
        universities = University.objects.all().order_by('name')
        paginator = Paginator(universities, UNIVERSITIES_PER_PAGE)
        page = self.request.GET.get('page')
        try:
            univs = paginator.page(page)
        except PageNotAnInteger:
            univs = paginator.page(1)
        except EmptyPage:
            univs = paginator.page(paginator.num_pages)
        context['universities'] = univs
        return context


class UniversityDetailTemplateView(TemplateView):
    template_name = 'universities/university_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UniversityDetailTemplateView, self).get_context_data(
                        *args, **kwargs)
        university = get_object_or_404(University, **kwargs)
        admissions = Admission.objects.filter(university=university)
        context['admissions'] = admissions
        context['university'] = university
        return context
