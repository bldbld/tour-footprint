#encoding: utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
from tourfp_web.views import web_index, web_reg, web_login, web_logout, web_createmap, web_help
from tourfp_map.views import showmap, show_add_tourset, show_add_place, show_add_trip, show_add_route, show_add_route_text
from tourfp_simplemap.views import get_simpleroute_list, get_simpleroute_list_line, save_simpleroute, delete_simpleroute, match_text
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tourfootprint.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', web_index, name='index'),
    
    # 系统操作
    url(r'^reg/', web_reg, name='reg'),
    url(r'^login/', web_login, name='login'),
    url(r'^logout/', web_logout, name='logout'),
    url(r'^help/', web_help, name='help'),
    
    # 创建地图 主页面
    url(r'^createmap/', web_createmap, name='createmap'),
    
    # 展示地图
    url(r'^showmap/', showmap, name='showmap'),
    # url(r'^showmap/', showsimplemap, name='showmap'),
    
    # 创建内容
    url(r'^oper/add_tourset/', show_add_tourset, name='add_tourset'),
    url(r'^oper/add_place/', show_add_place, name='add_place'),
    url(r'^oper/add_trip/', show_add_trip, name='add_trip'),
    url(r'^oper/add_route/', show_add_route_text, name='add_route'),
    
    
    url(r'^get_simpleroute_list/', get_simpleroute_list, name='get_simpleroute_list'),
    url(r'^get_simpleroute_list_line/', get_simpleroute_list_line, name='get_simpleroute_list_line'),
    url(r'^save_simpleroute/', save_simpleroute, name='save_simpleroute'),
    url(r'^delete_simpleroute/', delete_simpleroute, name='delete_simpleroute'),
    
    url(r'^match_text/', match_text, name='match_text'),
)
