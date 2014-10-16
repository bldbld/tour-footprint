#encoding: utf-8
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from tourfp_map.models import trip, route, place, tourset
from tourfp_map.mapmodels_forms import add_place_form, add_route_form, add_tourset_form, add_trip_form, add_route_text_form, add_route_simple_form
from tourfp_map.lbsservice import getCityPlaceByBaidu
from util import json_encode
import datetime
import json

# 地图显示及操作

################################################################################
# 显示地图
def showmap (request):
    t = get_template('baidu/map.html')
    # tourlist = tour.objects.all()
    # json.dumps(routearr, ensure_ascii=False).
    route_list = get_routelist()
    html = t.render(Context({'route_list': route_list}))
    return HttpResponse(html)

################################################################################
# 显示添加旅行集页面
def show_add_tourset(request):
    template_var = {}
    form = add_tourset_form()  
    print (request.method)  
    if request.method == 'POST' and request.user.is_authenticated:
        form = add_tourset_form(request.POST.copy())
        if form.is_valid():
            data = tourset(owner=request.user, title=form.cleaned_data["tourset_name"])
            data.save()
    template_var["form"] = form        
    return render_to_response("add_page.html", template_var, context_instance=RequestContext(request))

################################################################################
# 显示添加旅行页面
def show_add_trip(request):
    template_var = {}
    
    # 初始化表单
    form = add_trip_form()
    form.fields['trip_tourset'].widget.choices = get_tourset_list_by_user_list(request.user)
    # form = add_trip_form(tourset.objects.filter(owner=request.user))
    #  form.fields['trip_tourset'].choices = get_tourset_list_by_user_list(request.user)
    if request.method == 'POST' and request.user.is_authenticated:
        form = add_trip_form(request.POST.copy(), get_tourset_list_by_user_list(request.user))
        if form.is_valid():
            iditem = form.cleaned_data["trip_tourset"]
            toursetitem = tourset.objects.get(id=iditem)
            data = trip(owner=request.user,
                         # date = form.cleaned_data["trip_date"],
                         date=datetime.datetime.now(),
                         create_time=datetime.datetime.now(),
                         remark=form.cleaned_data["trip_remark"],
                         url='http://www.google.com',
                         tourset=toursetitem,
                         color='red',
                         weight=3
                         )
            data.save()
    template_var["form"] = form 
    template_var["select_id_list"] = "id_trip_tourset,"
    # template_var["tourset_list"] =  get_tourset_list_by_user(request.user)
    
    return render_to_response("add_page.html", template_var, context_instance=RequestContext(request))

################################################################################
# 显示添加路线页面
def show_add_route(request):
    template_var = {}
    form = add_route_form()    
    form.fields['route_place_from'].widget.choices = get_all_place()
    form.fields['route_place_to'].widget.choices = get_all_place()
    form.fields['route_trip'].widget.choices = get_trip_list_by_user_list(request.user)
    if request.method == 'POST' and request.user.is_authenticated:
        form = add_route_form(request.POST.copy())
        # form = add_route_form(request.POST.copy(), get_all_place(), get_all_place(), get_trip_list_by_user_list(request.user))
        print(form.is_valid())
        if form.is_valid():
            route_place_from_form_item = form.cleaned_data["route_place_from"]
            route_place_from_item = place.objects.get(id=route_place_from_form_item)
            route_place_to_form_item = form.cleaned_data["route_place_to"]
            route_place_to_item = place.objects.get(id=route_place_to_form_item)
            route_tour_form_item = form.cleaned_data["route_trip"]
            route_tour_item = trip.objects.get(id=route_tour_form_item)
            print(route_place_from_item)
            print(route_place_to_item)
            print(route_tour_item.__unicode__())
            data = route(place_from=route_place_from_item,
                         place_to=route_place_to_item
                         )
            data.save()
            data.tour.add(route_tour_item)
    template_var["form"] = form  
    template_var["select_id_list"] = "id_route_place_from,id_route_place_to,id_route_tour"      
    return render_to_response("add_page.html", template_var, context_instance=RequestContext(request))

################################################################################
# 显示添加路线页面（文本模式 ）
def show_add_route_text(request):
    template_var = {}
    form = add_route_text_form()    
    form.fields['route_trip'].widget.choices = get_trip_list_by_user_list(request.user)
    if request.method == 'POST' and request.user.is_authenticated:
        form = add_route_text_form(request.POST.copy())
        # form = add_route_form(request.POST.copy(), get_all_place(), get_all_place(), get_trip_list_by_user_list(request.user))
        print(form.is_valid())
        if form.is_valid():
            route_place_from_form_item = form.cleaned_data["route_place_from"]
            route_place_from_item = getCityPlaceByBaidu(route_place_from_form_item)
            route_place_to_form_item = form.cleaned_data["route_place_to"]
            route_place_to_item = route_place_from_form_item(route_place_to_form_item)
            route_tour_form_item = form.cleaned_data["route_trip"]
            route_tour_item = trip.objects.get(id=route_tour_form_item)
            print(route_place_from_item)
            print(route_place_to_item)
            print(route_tour_item.__unicode__())
            data = route(place_from=route_place_from_item,
                         place_to=route_place_to_item
                         )
            data.save()
            data.tour.add(route_tour_item)
    template_var["form"] = form  
    template_var["select_id_list"] = "id_route_place_from,id_route_place_to,id_route_tour"      
    return render_to_response("add_page.html", template_var, context_instance=RequestContext(request))

################################################################################
# 显示添加路线页面（简单）
def show_add_route_simple(request):
    template_var = {}
    form = add_route_simple_form()  
    print (request.method)  
    if request.method == 'POST' and request.user.is_authenticated:
        form = add_route_simple_form(request.POST.copy())
        if form.is_valid():
            # 保存起点
            route_place_from_form_item = form.cleaned_data["route_place_from"]
            route_place_from_item = getCityPlaceByBaidu(route_place_from_form_item)
            # 保存 
            route_place_to_form_item = form.cleaned_data["route_place_to"]
            route_place_to_item = route_place_from_form_item(route_place_to_form_item)
            route_place_to_item.save()
            # route_tour_item = trip.objects.get(id=route_tour_form_item)
            data = route(place_from=route_place_from_item,
                         place_to=route_place_to_item
                         )
            data.save()
            # data.tour.add(route_tour_item)
    template_var["form"] = form        
    return render_to_response("simple_add_page.html", template_var, context_instance=RequestContext(request))


################################################################################
# 显示添加地点页面
def show_add_place(request):
    template_var = {}
    form = add_place_form()    
    if request.method == 'POST' and request.user.is_authenticated:
        form = add_place_form(request.POST.copy())
        if form.is_valid():
            data = place(title=form.cleaned_data["place_title"],
                            lng=form.cleaned_data["place_lng"],
                            lat=form.cleaned_data["place_lat"],
                            is_manual=True,
                            update_time=datetime.datetime.now()
                            )
            data.save()
    template_var["form"] = form        
    return render_to_response("add_page.html", template_var, context_instance=RequestContext(request))

################################################################################
# 得到旅行的全部路线
def get_routelist(trip):
    routelist = route.objects.filter(tour=trip)
    routearr = []
    for one_route in routelist:
        place_from = one_route.place_from
        place_to = one_route.place_to
        routearr.append(place_from.lng)
        routearr.append(place_from.lat)
        routearr.append(place_to.lng)
        routearr.append(place_to.lat)
    return tuple(routearr)

################################################################################
# 得到旅行的全部路线
def get_default_routelist(user):
    routelist = route.objects.filter(tour=user)
    routearr = []
    for one_route in routelist:
        place_from = one_route.place_from
        place_to = one_route.place_to
        routearr.append(place_from.lng)
        routearr.append(place_from.lat)
        routearr.append(place_to.lng)
        routearr.append(place_to.lat)
    return tuple(routearr)

################################################################################
# 
def get_tourset_list_by_user_list(user):
    tourset_list_q = tourset.objects.filter(owner=user)
    tourset_list_ret = []
    for one_tourset in tourset_list_q:
        tourset_r = (one_tourset.id, one_tourset.title)
        tourset_list_ret.append(tourset_r)
    return tourset_list_ret
    # return tuple(tourset_list_ret)

# def get_tourset_list_by_user(user):
#    tourset_list = tourset.objects.filter(owner=user)
#    return str(json_encode.json_encode(tourset_list))

################################################################################
#
def get_trip_list_by_user_list(user):
    trip_list_q = trip.objects.filter(owner=user)
    trip_list_ret = []
    for item_q in trip_list_q:
        item_ret = (item_q.id, item_q.remark)
        trip_list_ret.append(item_ret)
    return trip_list_ret 
    
### ### ###
#
def get_all_place():
    place_list_q = place.objects.all()
    place_list_ret = []
    for item_q in place_list_q:
        item_ret = (item_q.id, item_q.title)
        place_list_ret.append(item_ret)
    return place_list_ret
