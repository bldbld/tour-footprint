from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from tourfp_simplemap.models import SimpleRoute
from tourfp_simplemap.lbsservice import getCityPlaceByBaidu, SimplePoint
import json

################################################################################
# 显示地图
def showsimplemap (request):
    t = get_template('baidu/map.html')
    # tourlist = tour.objects.all()
    # json.dumps(routearr, ensure_ascii=False).
    route_list = get_routelist(request.user)
    html = t.render(Context({'route_list': route_list}))
    return HttpResponse(html)

# 获取路线列表JSON，用于显示地图
def get_simpleroute_list_line(request):
    route_list_q = SimpleRoute.objects.filter(owner=request.user)
    json_str = "{'route':["
    for item_q in route_list_q:
        json_str = json_str + item_q.to_json_line() + ','
    json_str = json_str + ']}'
    # jsondict={'lat':'123','save_name':'ab'} 
    return HttpResponse(json.dumps(json_str, ensure_ascii = False))  
    
# 获取路线列表JSON，用于显示标题
def get_simpleroute_list(request):
    route_list_q = SimpleRoute.objects.filter(owner=request.user)
    json_str = "{'route':["
    for item_q in route_list_q:
        json_str = json_str + item_q.to_json_brief() + ','
    json_str = json_str + ']}'
    # jsondict={'lat':'123','save_name':'ab'} 
    return HttpResponse(json.dumps(json_str, ensure_ascii = False))  

# 保存一条路线
def save_simpleroute(request):
    startName = request.GET.get("startName")
    print(startName)
    endName = request.GET.get("endName")
    print(endName)
    # startPoint = SimplePoint()
    # endPoint = SimplePoint()
    startPoint = getCityPlaceByBaidu(startName);
    print(startPoint.lat)
    endPoint = getCityPlaceByBaidu(endName);
    print(endPoint.lat)
    sr = SimpleRoute(from_title = startName, from_lng = startPoint.lng, from_lat = startPoint.lat,
                        to_title = endName, to_lng = endPoint.lng, to_lat = endPoint.lat, owner = request.user)
    print(1)
    print(sr.to_json_brief())
    print(sr.to_json_line())
    sr.save()
    return HttpResponse()  

def deleteSimpleRoute(request):
    return