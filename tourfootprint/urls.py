#encoding: utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
from tourfp_web.views import web_index, web_reg, web_login, web_logout, webShowmap, web_help, html_login_submit, html_reg_submit
from tourfp_simplemap.views import get_simpleroute_list, get_simpleroute_list_line, save_simpleroute, delete_simpleroute, match_text
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tourfootprint.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', web_index),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', web_index, name='index'),
    
    # 系统操作
    url(r'^reg/', web_reg, name='reg'),
    url(r'^login/', web_login, name='login'),
    url(r'^logout/', web_logout, name='logout'),
    url(r'^help/', web_help, name='help'),
    
    url(r'^html_login_submit/', html_login_submit, name='html_login_submit'),
    url(r'^html_reg_submit/', html_reg_submit, name='html_reg_submit'),
    
    
    # 创建地图 主页面
    url(r'^createmap/', webShowmap, name='createmap'),
    url(r'^people/\w+/map/', webShowmap, name='people_map'),#\w  = [a-zA-Z0-9_]
    
    # 创建内容
    url(r'^get_simpleroute_list/', get_simpleroute_list, name='get_simpleroute_list'),
    url(r'^get_simpleroute_list_line/', get_simpleroute_list_line, name='get_simpleroute_list_line'),
    url(r'^save_simpleroute/', save_simpleroute, name='save_simpleroute'),
    url(r'^delete_simpleroute/', delete_simpleroute, name='delete_simpleroute'),
    
    url(r'^match_text/', match_text, name='match_text'),
)
