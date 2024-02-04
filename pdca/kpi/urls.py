from django.urls import path

from .views import get_all_real_kpi, get_main_page, get_all_glide_kpi, get_choice_page, postitem


urlpatterns = [
    path("", get_main_page, name="home"),
    path("kpi-link-page/<slug:slug>",get_choice_page, name='linkpage' ),
    path("kpi-enter/<slug:slug>/real",get_all_real_kpi, name='real_kpi' ),
    path("kpi-enter/<slug:slug>/glide",get_all_glide_kpi, name='glide_kpi' ),
    path('test',postitem,name='test')
]
