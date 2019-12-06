from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
# 首页（登录）
def index(request):
    return render(request, "index.html")

# 登录动作
def login_action(request):
    # 第一步 判断请求的方法
    if request.method == "POST":
        # 接收用户输入的用户名、密码（方法要与页面提交的方法一致），username对应前端输入框标签的name="username"，
        # 寻找名为 "username"和"password"的POST参数，而且如果参数没有提交，返回一个空的字符串。
        username = request.POST.get("username","")  
        password = request.POST.get("password","")
        # print("username: "+username)
        # print("password: "+password)
        #第二步 判空，如果输入的内容有空的，直接提示
        if username == "" or password == "":
            # key error相当于发送给客户端的变量，变量对应的值就是后面的value
            return render(request, "index.html", {"error":"username or password null!"})
        # 第三步 有输入用户名和密码，那么去数据库查前端传过来的用户名和密码，
        else:
            user = auth.authenticate(username = username, password = password)
            # 第四步 用户名和密码在数据库有查到，那么进行验证
            if user is not None:
                # 验证登录
                auth.login(request, user)
                #验证通过就重定向到发布会管理页面
                response = HttpResponseRedirect('/event_manage/')  # 返回302
                # 添加浏览器 cookie，10分钟过期
                # response.set_cookie('user',username,600)
                # 将session信息记录到浏览器    session的信息是存在服务器端的数据库的
                request.session['user'] = username
                # 最后返回发布会管理页面给前端，浏览器进行渲染呈现
                return response
            else:
                return render(request, "index.html", {"error":"username or password error!"})
    else:
        return render(request, "index.html")

# 发布会管理(登录之后的默认页面)
@login_required    # 关窗，无法直接访问登录成功的页面（在浏览器地址栏直接回车访问event_manage）
def event_manage(request):
    # 读取浏览器 cookie
    # username = request.COOKIES.get('user', '')
    # 读取浏览器 session
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {"user":username, "events":event_list})

#退出系统
@login_required
def logout_action(request):
    # 退出并清除掉浏览器保存的用户信息
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response

# 发布会名称搜索
@login_required()
def search_name(request):
    username = request.session.get('user', '')
    name = request.GET.get("name", '')
    # print(name)
    search_name_result = Event.objects.filter(name__contains = name)
    if len(search_name_result) == 0:
        return render(request, "event_manage.html", {"user":username, "hint":"搜索‘发布会名称’查询结果为空！","events":search_name_result})
    return render(request, "event_manage.html", {"user":username, "events":search_name_result})

# 嘉宾管理
@login_required()
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list,2)  # 如果嘉宾的信息不够2条，就会报一个警告信息，见models
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型，返回第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # r如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user":username, "guests":contacts})

#嘉宾手机号的查询
@login_required()
def search_phone(request):
    username = request.session.get('user', '')
    search_phone = request.GET.get("phone", '')
    # search_name_bytes = search_phone.encode(encoding="utf-8")
    search_phone_result = Guest.objects.filter(phone__contains = search_phone)
    if len(search_phone_result) == 0:
        return render(request, "guest_manage.html", {"user":username, "hint":"搜索‘手机号’查询结果为空！","phone":search_phone})
    # print(search_phone_result)
    paginator = Paginator(search_phone_result,2)
    page = request.GET.get('page','')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型，返回第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user":username, "guests":contacts,"phone":search_phone})

'''
嘉宾签到页面：http://127.0.0.1:8000/sign_index/4/        event_manage.html: href="/sign_index/{{ event.id }}/"
签到页面和其他的页面不同，除了request（接口是从urls拿的），还要一个event_id,这个event_id不是
像{domain}/?event_id=2这种跟在url后面通过get请求拿到的key=value形式,是直接在路径里面的，不能像前面那样request.GET.get去接收，
http://127.0.0.1:8000/sign_index/4/这种形式的参数怎么接收呢？需要在request里面后面去拼。
'''
# 嘉宾签到页面
@login_required()
def sign_index(request, event_id):    # event_id是通过路径里面抓取的
    event = get_object_or_404(Event, id=event_id)
    # event_id发布会的签到人数（已签+未签）
    guest_list = Guest.objects.filter(event_id=event_id)
    # event_id发布会的已签到人数
    sign_list = Guest.objects.filter(sign='1', event_id=event_id)
    guest_data = str(len(guest_list))
    sign_data = str(len(sign_list))

    return render(request, "sign_index.html",{'event':event,
                                              'guest':guest_data,
                                              'sign':sign_data})

'''
get_object_or_404的介绍： 我们原来调用django 的get方法(model.object.get())，如果查询的对象不存在的话，
会抛出一个DoesNotExist的异常， 现在我们调用django get_object_or_404方法，它会默认的调用django 的get方法，
如果查询的对象不存在的话，会抛出一个Http404的异常，我感觉这样对用户比较友好， 如果用户查询某个产品不存在的话，
我们就显示404的页面给用户，比直接显示异常好。
'''

# 签到动作
@login_required
def sign_index_action(request,event_id):
    event = get_object_or_404(Event, id=event_id)
    # event_id发布会的签到人数（已签+未签）
    guest_list = Guest.objects.filter(event_id=event_id)
    guest_data = str(len(guest_list))
    sign_data = 0   #计算发布会“已签到”的数量
    for guest in guest_list:
        if guest.sign == True:
            sign_data += 1

    phone =  request.POST.get('phone','')
    # print(phone)
    results = Guest.objects.filter(phone = phone)
    # print("======================", results)
    if not results:
        return render(request, 'sign_index.html', {'event': event,'hint': 'phone error.','guest':guest_data,'sign':sign_data})
    try:
        Guest.objects.get(phone = phone,event_id = event_id)
    except Exception:    # 不知道具体啥异常
        return render(request, 'sign_index.html', {'event': event,'hint': 'event id or phone error.','guest':guest_data,'sign':sign_data})

    # if not result:
    #     return render(request, 'sign_index.html', {'event': event,'hint': 'event id or phone error.','guest':guest_data,'sign':sign_data})

    result = Guest.objects.get(event_id = event_id,phone = phone)

    if result.sign:
        return render(request, 'sign_index.html', {'event': event,'hint': "user has sign in.",'guest':guest_data,'sign':sign_data})
    else:
        Guest.objects.filter(event_id = event_id,phone = phone).update(sign = '1')
        return render(request, 'sign_index.html', {'event': event,'hint':'sign in success!',
            'user': result,
            'guest':guest_data,
            'sign':str(int(sign_data)+1)
            })

'''
get方法是从数据库的取得一个匹配的结果，返回一个对象，如果记录不存在的话，它会报错。
filter方法是从数据库的取得匹配的结果，返回一个对象列表，如果记录不存在的话，它会返回[]。
'''







