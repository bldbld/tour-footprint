#encoding: utf-8
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from tourfp_web.forms import RegisterForm, LoginForm
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.core.context_processors import csrf

# Create your views here.

def web_index(request):
    template_var={}
    template_var["w"]=_("Welcome")
    if request.user.is_authenticated():     #判断用户是否已登录  
        template_var["w"]=_("Welcome %s!")%request.user.username
    else:     
        print('no')           #非登录用户将返回AnonymousUser对象  
    t = get_template('index.html')
    #html = t.render(RequestContext(request))
    #return HttpResponse(html)
    return render_to_response("index.html",template_var,context_instance=RequestContext(request))

def web_about(request):
    t = get_template('contacts.html')
    html = t.render(Context({}))
    return HttpResponse(html)

# 注册网站
def web_reg(request):
    template_var = {}
    form = RegisterForm()    
    if request.method == "POST":
        form = RegisterForm(request.POST.copy())
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username, email, password)
            user.save()
            _login(request, username, password)  # 注册完毕 直接登陆
            return HttpResponseRedirect(reverse("index"))    
    template_var["form"] = form        
    return render_to_response("reg.html", template_var, context_instance=RequestContext(request))

def web_login(request):
    '''登陆视图'''
    template_var = {}
    form = LoginForm()    
    if request.method == 'POST':
        form = LoginForm(request.POST.copy())
        if form.is_valid():
            _login(request, form.cleaned_data["username"], form.cleaned_data["password"])
            return HttpResponseRedirect(reverse("index"))
    template_var["form"] = form        
    return render_to_response("login.html", template_var, context_instance=RequestContext(request))

def web_logout(request):
    '''注销视图'''
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))

# 使用HTML网页进行登录
def html_login_submit(request):
    '''登录'''
    username = request.POST.get("username")
    password = request.POST.get("password")
    ret = _login(request, username, password)
    template_var={}
    if ret:
        template_var["w"]=_("Welcome %s!")%request.user.username
        #return render_to_response("index.html",template_var,context_instance=RequestContext(request))
        return HttpResponseRedirect(reverse("index"))    
    else: 
        return render_to_response("login.html",context_instance=RequestContext(request))

# 使用HTML网页进行注册
def html_reg_submit(request):
    '''注册'''
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    user = User.objects.create_user(username, email, password)
    user.save()
    _login(request, username, password)  # 注册完毕 直接登陆
    return HttpResponseRedirect(reverse("index"))    

def web_help(request):
    return 

# 地图主界面
def web_createmap(request):
    template_var = {}
    return render_to_response("createmap_simple.html",template_var,context_instance=RequestContext(request))

def _login(request, username, password):
    '''登陆核心方法'''
    ret = False
    user = authenticate(username=username, password=password)
    print(user)
    if user:
        if user.is_active:
            auth_login(request, user)
            ret = True
        else:
            messages.add_message(request, messages.INFO, _("用户没有激活"))
    else:
        messages.add_message(request, messages.INFO, _("用户不存在"))
    return ret
    
def logout(request):
    '''注销视图'''
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))
