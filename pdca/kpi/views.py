from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import Department, KPIValue


from .service import DepartmentService, KPIservice


deprtment_serviece = DepartmentService()
kpi_serviece = KPIservice()


def get_main_page(request: HttpRequest) -> HttpResponse:
    context = {"departments": deprtment_serviece.fetch_all()}
    template_name = "kpi/index.html"
    return render(request, context=context, template_name=template_name)


def get_choice_page(request: HttpRequest, slug) -> HttpResponse:
    if not slug:
        return redirect("home")
    try:
        department = deprtment_serviece.fetch_one(slug, is_slug=True)
        context = {"department": department}
        template_name = "kpi/link_page.html"
    except Department.DoesNotExist:
        return redirect("home")
    else:
        return render(request, context=context, template_name=template_name)


def get_ch(month, kpi):
    try:
        return KPIValue.objects.get(kpi_phase=month, kpi=kpi)
    except KPIValue.DoesNotExist:
        return None


def get_all_real_kpi(request: HttpRequest, slug: str) -> HttpResponse:
    if not slug:
        return redirect("home")
    try:
        header, body = kpi_serviece.get_kpi_matrix(slug, is_glide=False)
        context = {
            "header": header,
            "body": body,
            "department": deprtment_serviece.fetch_one(slug, is_slug=True),
        }
        template = "kpi/real_kpi_table.html"
    except Department.DoesNotExist:
        return redirect("home")
    else:
        return render(request, context=context, template_name=template)


def get_all_glide_kpi(request: HttpRequest, slug: str) -> HttpResponse:
    if not slug:
        return redirect("home")
    try:
        header, body = kpi_serviece.get_kpi_matrix(slug, is_glide=True)
        context = {
            "header": header,
            "body": body,
            "department": deprtment_serviece.fetch_one(slug, is_slug=True),
        }
        template = "kpi/real_kpi_table.html"
    except Department.DoesNotExist:
        return redirect("home")
    else:
        return render(request, context=context, template_name=template)


def postitem(request: HttpRequest):
    a = request.POST.dict()
    print(a)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))