from sign.models import Event,Guest
from django.http import JsonResponse
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import time
from django.db.utils import IntegrityError

#添加发布会接口
'''

'''
def add_event(request):
    eid = request.POST.get('eid', '')                  # 发布会id
    name = request.POST.get('name', '')                # 发布会标题
    limit = request.POST.get('limit', '')              # 限制人数
    status = request.POST.get('status', '')            # 状态
    address = request.POST.get('address', '')          # 地址
    start_time = request.POST.get('start_time', '')    # 发布会时间

    if eid == '' or name == '' or limit == '' or address=='' or start_time == '':
        return JsonResponse({"status":10021, "message":"参数为空."})

    ''' 入参类型处理 '''
    try:
        int(eid)
    except ValueError:
        return JsonResponse({"status":10026, "message":"eid参数类型错误."})

    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({"status":10023, "message":"发布会ID已存在."})

    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({"status":10024, "message":"发布会名称已存在."})
    if status == '':
        status = 1    # 不传status默认开启
    try:
        Event.objects.create(id=eid, name=name, limit=limit, status=int(status), address=address, start_time=start_time)
    except ValidationError:
        error = '日期时间格式错误，参考格式：YYYY-MM-DD HH:MM:SS.'
        return JsonResponse({'status':10025,'message':error})
    return JsonResponse({'status':200,'message':'add event success.'})

# 发布会查询接口（发布会ID或者名称至少要有一个）
def get_event_list(request):
    eid = request.GET.get('eid', '')
    name = request.GET.get('name', '')
    if eid == '' and name == '':
        return JsonResponse({"status":10021, "message":"参数错误."})
    if eid != '':
        # 把发布会信息存在event字典里，然后作为另一个字典的某个key的value，JsonResponse方法直接把字典转为json发给前端
        event = {}
        try:
            int(eid)
        except ValueError:
            return JsonResponse({"status":10026, "message":"eid参数类型错误."})
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022, 'message':'查询结果为空.'})
        else:
            event['eid'] = result.id
            event['name'] = result.name
            event['limit'] = result.limit
            event['status'] = result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            print(event)
            return JsonResponse({'status':200, 'message':'success.', 'data':event})
    if name != '':
        datas = []
        results = Event.objects.filter(name__contains=name)
        if results:
            print("=========================")
            print(results)
            for r in results:
                print("----------------------------")
                print(r)
                event = {}
                event['eid'] = r.id
                event['name'] = r.name
                event['limit'] = r.limit
                event['status'] = r.status
                event['address'] = r.address
                event['start_time'] = r.start_time
                datas.append(event)
            print(datas)
            return JsonResponse({'status':200, 'message':'success.', 'data':datas})
        else:
            return JsonResponse({'status':10022, 'message':'查询结果为空.'})

# 添加嘉宾接口
'''嘉宾参加发布会需要哪些条件？
1.发布会存在
2.发布会状态未过期
3.发布会会场有空座位
4.发布会时间要小于等于当前时间
5.嘉宾没有参加过该场发布会（该发布会没有某嘉宾电话）
'''
def add_guest(request):
    eid = request.POST.get('eid', '')              # 关联发布会id
    realname = request.POST.get('realname', '')    # 姓名
    phone = request.POST.get('phone', '')          # 手机号
    email = request.POST.get('email', '')          # 邮箱
    if eid == '' or realname == '' or phone == '':
        print("-----入参叛空-----")
        return JsonResponse({"status":10021, "message":"参数为空."})
    try:
        print("-----eid类型处理-----")
        int(eid)
    except ValueError:
        return JsonResponse({"status":10026, "message":"eid参数类型错误."})
    print("-----判断发布会是否存在 -----")
    result = Event.objects.filter(id=eid)
    print("-----发布会信息：", result)
    if not result:
        return JsonResponse({"status":10022, "message":"发布会不存在."})
    result = Event.objects.get(id=eid).status
    print("-----发布会的状态：", result)
    if not result:
        return JsonResponse({"status":10023, "message":"发布会已过期."})
    event_limit = Event.objects.get(id=eid).limit       # 发布会限制人数
    guest_limit = Guest.objects.filter(event_id=eid)    # 发布会已添加的嘉宾数
    print("-----发布会会场人数上限：", event_limit)
    print("-----发布会已参加人数：", len(guest_limit))
    if len(guest_limit) >= event_limit:
        return JsonResponse({"status":10024, "message":"发布会座位已售空."})
    event_time = Event.objects.get(id=eid).start_time    # 发布会时间
    print("-----发布会开始时间: ", event_time)
    time_tuple = time.strptime(str(event_time), "%Y-%m-%d %H:%M:%S")
    print("-----发布会开始时间转换为结构化时间元组: ", time_tuple)
    e_time = int(time.mktime(time_tuple))
    print("-----结构化时间元组转化为时间戳: ", e_time)
    n_time = int(time.time())      # 当前时间
    if n_time >= e_time:
        return JsonResponse({'status':10025,'message':'event has started'})
    try:
        Guest.objects.create(realname=realname,phone=int(phone),email=email,sign=0,event_id=int(eid))
    except IntegrityError:
        return JsonResponse({'status':10026,'message':'该场发布会该嘉宾电话已存在'})

    return JsonResponse({'status':200,'message':'添加嘉宾成功'})

# 嘉宾查询接口
'''
1.通过手机号查询嘉宾

'''
def get_guest_list(request):
    eid = request.GET.get('eid', '')        # 关联发布会id
    phone = request.GET.get('phone', '')    # 嘉宾手机号
    print("-----eid: ", eid)
    print("-----phone: ", phone)
    if eid == '':
        return JsonResponse({'status':10021,'message':'eid不能为空'})

    if eid != '' and phone == '':
        try:
            print("-----eid类型处理-----")
            int(eid)
        except ValueError:
            return JsonResponse({"status":10026, "message":"eid参数类型错误."})
        datas = []
        results = Guest.objects.filter(event_id=eid)
        if results:
            guest = {}
            for r in results:
                guest['realname'] = r.realname
                guest['phone'] = r.phone
                guest['email'] = r.email
                guest['sign'] = r.sign
                datas.append(guest)
            return JsonResponse({'status':200, 'message':'success.', 'data':datas})
        else:
            return JsonResponse({'status':10022, 'message':'查询结果为空.'})
    if eid != '' and phone != '':
        guest = {}
        try:
            result = Guest.objects.get(phone=phone, event_id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022, 'message':'查询结果为空.'})
        else:
            guest['realname'] = result.realname
            guest['phone'] = result.phone
            guest['email'] = result.email
            guest['sign'] = result.sign
            return JsonResponse({'status':200, 'message':'success.', 'data':guest})

# 用户签到接口
'''
1.发布会ID不能为空
2.手机号不能为空
3.发布会为int类型，phone是使用filter检索的，传字符串给phone没事
4.发布会的status为1是有效的，为0是关闭的
5.发布会的开始时间start_time小于当前时间
6.start_time大于当前时间，发布会已开始或者已经结束
'''
def user_sign(request):
    eid = request.POST.get('eid', '')
    phone = request.POST.get('phone', '')
    # 1.eid和phone都不能为空
    if eid == '' or phone == '':
        return JsonResponse({'status':10021,'message':'参数不能为空'})
    # 2.eid 非int型异常处理
    try:
        int(eid)
    except ValueError:
        return JsonResponse({"status":10026, "message":"eid参数类型错误."})
    # 3.发布会ID在发布会表没有找到，即发布会不存在
    try:
        result = Event.objects.get(id=eid)
    except Event.DoesNotExist:
        return JsonResponse({'status': 10022, 'message': 'event id null'})
    # 4.发布会的状态是关闭的
    if result.status is False:
        return JsonResponse({'status': 10023, 'message': 'event status is not available'})
    # 5.发布会的时间是小于当前时间的，如果大于当前时间，就是已经开始或者结束了
    event_time = result.start_time    # 发布会时间
    print("-----发布会开始时间: ", event_time)
    time_tuple = time.strptime(str(event_time), "%Y-%m-%d %H:%M:%S")
    print("-----把发布会开始时间转换为结构化时间元组: ", time_tuple)
    e_time = int(time.mktime(time_tuple))
    print("-----再把结构化时间元组转化为时间戳: ", e_time)
    n_time = int(time.time())   # 当前时间
    if n_time >= e_time:
        return JsonResponse({'status':10024,'message':'event has started or end'})
    # 6.手机号在嘉宾表检索嘉宾，判断检索结果result列表是否为空
    result = Guest.objects.filter(phone=phone)
    if not result:
        return JsonResponse({'status':10025,'message':'user phone null'})
    # 7.手机号检索到的嘉宾不为空
    else:
        for res in result:
            if res.event_id == int(eid):
                break
        else:  # for循环遍历完并为空（res）时执行
            return JsonResponse({'status': 10026, 'message': 'user did not participate in the conference'})

    result = Guest.objects.get(event_id=eid, phone=phone)
    if result.sign is True:
        return JsonResponse({'status':10027,'message':'user has sign in'})
    else:
        result.sign = True
        result.save()
        return JsonResponse({'status':200,'message':'sign success'})


'''当迭代的对象迭代完并为空时，位于else的子句将执行，而如果在for循环中含有break时则直接终止循环，
并不会执行else子句。

for i in range(10):
    if i == 5:
        print('found it! i = %s' % i)
        break
else:
    print('not found it ...')
'''
