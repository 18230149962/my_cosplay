from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "index.html")
# 登录

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            # response.set_cookie('user',username,3600) #添加浏览器cookies
            request.session['user'] = username #将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': '输入错了，老铁'})

# 发布会管理
@login_required
def event_manage(request):
    # username = request.COOKIES.get('user', '') #读取浏览器cookies
    event_list = Event.objects.all()
    username = request.session.get('user', '') #读取session的值
    return render(request, "event_manage.html", {"user":username,
                                                 "events":event_list})
