from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404
from django.template import loader
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from .models import *

site_settings = {
    "name": settings.PORTFOLIO_NAME,
    "accreditation": settings.PORTFOLIO_ACCREDITATION,
    "title": settings.PORTFOLIO_TITLE,
    "email": settings.PORTFOLIO_EMAIL,
    "github": settings.PORTFOLIO_GITHUB,
    "linkedin": settings.PORTFOLIO_LINKEDIN,
    "about": settings.PORTFOLIO_ABOUT,
}

def index(request):
    sections = Section.objects.filter(active=True)
    template = loader.get_template('main/index.html')
    context = {'sections': sections, 'site_settings': site_settings}
    return HttpResponse(template.render(context, request))


def detail(request, slug):
    try:
        section = Section.objects.get(slug=slug)
    except Section.DoesNotExist:
        raise Http404("page does not exist")
    try:
    	code_template = mark_safe(render_to_string('main/'+section.slug+'.html'))
    except:
    	code_template = ""

    return render(
        request,
        'main/detail.html',
        {
            'section': section,
            'code_example': code_template,
            'site_settings': site_settings
        }
    )
