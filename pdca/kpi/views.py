from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .repository import DepartmentRepository

from .service import DepartmentService

deprtment_servie = DepartmentService(DepartmentRepository)


# Create your views here.
# def get_all_real_kpi(request: HttpRequest) -> HttpResponse:
    # template = ''
    # if req
    # context = KPIrepo.fetch_real(cat)
    # return render(context,template)


def render_main_page(request: HttpRequest) -> HttpResponse:

    context = {'departments': deprtment_servie.fetch_all()}

    template_name = 'kpi/index.html'
    return render(request,context=context,template_name=template_name)