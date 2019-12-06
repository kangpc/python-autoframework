from django.test import TestCase
from django.contrib.auth.models import User
from sign.models import Event, Guest

# Create your tests here.
# 写django的单元测试
'''
django运行单元测试的时候不会真的查询数据库,必须初始化数据，才能真正登陆成功
比如登录接口需要去数据库查用户名和密码，没有真正去数据库查，只能跑用例前初始化auth_user表(用户名和密码)的数据。
'''

class ModelTest(TestCase):
    '''模型测试'''

    def setUp(self):
        Event.objects.create(id=1, name="oneplus 3 event", status=True, limit=2000, address='shenzhen', start_time='2016-08-31 02:18:22')
        Guest.objects.create(id=1, event_id=1, realname='alen', phone='13711001101',email='alen@mail.com', sign=False)

    def test_event_models(self):
        '''测试发布会表'''
        result = Event.objects.get(name="oneplus 3 event")
        self.assertEqual(result.address, "shenzhen")
        self.assertTrue(result.status)

    def test_guest_models(self):
        '''测试嘉宾表'''
        result = Guest.objects.get(phone='13711001101')
        self.assertEqual(result.realname, "alen")
        self.assertFalse(result.sign)

class IndexPageTest(TestCase):
    ''' 测试index登录首页 '''

    def test_index_page_renders_index_template(self):
        ''' 断言是否用给定的index.html模版响应 '''
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class LoginActionTest(TestCase):
    ''' 测试登录动作 '''

    def setUp(self):
        User.objects.create_user(username="kpc",email="kpc@mail.com",password="1234")

    def test_add_user_username_email(self):
        ''' 测试初始化的用户名和邮箱 '''
        user = User.objects.get(username="kpc")
        self.assertEqual(user.username,"kpc")
        self.assertEqual(user.email,"kpc@mail.com")

    def test_login_username_password_null(self):
        ''' 用户名密码为空 '''
        response = self.client.post('/login_action/', data={'username': '', 'password': ''})
        self.assertEqual(response.status_code, 200)
        # print(response.content)
        self.assertIn(b'username or password null!',response.content)

    def test_login_username_password_error(self):
        ''' 用户名密码错误 '''
        response = self.client.post('/login_action/', data={'username': 'kpc', 'password': '111'})
        self.assertEqual(response.status_code, 200)
        # print(dir(response))
        self.assertIn(b'username or password error!', response.content)

    def test_login_success(self):
        ''' 登录成功 '''
        user_info = {'username': 'kpc', 'password': '1234'}
        response = self.client.post('/login_action/', data=user_info)
        # print(response)
        self.assertEqual(response.status_code, 302)

class EvenManageTest(TestCase):
    '''发布会管理'''

    def setUp(self):
        '''初始化发布会管理的数据'''
        User.objects.create_user('kpc', 'kpc@mail.com', '1234')  # 前置条件是需要登录
        Event.objects.create(name='nubia9', limit='9000', status=0, address='xiamen', start_time='2019-01-10 14:00:00')
        user_info = {'username': 'kpc', 'password': '1234'}
        self.client.post('/login_action/', data=user_info)

    def test_add_event_data(self):
        '''测试添加发布会'''
        user = User.objects.get(username='kpc')
        event = Event.objects.get(name='nubia9')
        self.assertEqual(user.username, 'kpc')
        self.assertEqual(event.address, 'xiamen')

    def test_event_manage_success(self):
        ''' 测试发布会：nubia X 发布会 '''
        response = self.client.get('/event_manage/')
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"nubia9", response.content)
        self.assertIn(b"xiamen", response.content)

    def test_event_manage_search_success(self):
        ''' 测试发布会搜索 '''
        response = self.client.get('/search_name/', {'name': 'nubia9'})
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"nubia9", response.content)
        self.assertIn(b'xiamen', response.content)

class GuestManageTest(TestCase):
    ''' 嘉宾管理 '''

    def setUp(self):
        ''' 构造发布会和嘉宾的数据 '''
        User.objects.create_user('kpc', 'kpc@mail.com', '1234')
        Event.objects.create(name='nubia9', limit='9000', status=0, address='xiamen', start_time='2019-01-10 14:00:00')
        Guest.objects.create(realname='zhangailing',phone=13913301321,email='zal@mail.com',sign=False,event_id=7)
        self.client.post('/login_action/', data={'username': 'kpc', 'password': '1234'})

    def test_add_guest_data(self):
        ''' 测试添加嘉宾 '''
        guest = Guest.objects.get(realname='zhangailing')
        # print(guest)
        self.assertEqual(guest.email, 'zal@mail.com')
        self.assertEqual(guest.phone, '13913301321')
        self.assertFalse(guest.sign, msg='zhangailing signed')

    def test_guest_manage_success(self):
        ''' 测试嘉宾信息：zhangailing '''
        response = self.client.get('/guest_manage/')
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'zhangailing', response.content)
        self.assertIn(b'13913301321', response.content)

    def test_guest_manage_search_success(self):
        ''' 测试嘉宾搜索: zhangailing '''
        response = self.client.get('/search_phone/', phone='13913301321')
        # print(response)
        # print(response.content)
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'zhangailing', response.content)
        self.assertIn(b'13913301321', response.content)

class SignIndexActionTest(TestCase):
    ''' 发布会签到 '''

    def setUp(self):
        ''' 构造嘉宾签到的数据 '''
        User.objects.create_user(username='kpc', email='kpc@mail.com', password='1234')
        Event.objects.create(id=3, name='nubia9', limit=9000, status=1, address='xiamen', start_time='2019-01-10 14:00:00')
        Event.objects.create(id=7, name='nubia X Pro',limit=2000,status=1,address='xiamen',start_time='2019-04-13 15:48:37')
        Guest.objects.create(realname='dulala',phone=13913301322,email='dll@mail.com',sign=False,event_id=3)
        Guest.objects.create(realname='adu',phone=16666666666,email='ad@mail.com',sign=True,event_id=7)
        self.client.post('/login_action/', data={'username': 'kpc', 'password': '1234'})

    def test_add_data(self):
        ''' 测试初始化的数据 '''
        usr = User.objects.get(username='kpc')
        event = Event.objects.get(name='nubia9')
        guest = Guest.objects.get(realname='dulala')
        self.assertEqual('kpc@mail.com', usr.email)
        self.assertEqual('xiamen', event.address)
        self.assertEqual('13913301322', guest.phone)

    def test_sign_index_action_phone_null(self):
        ''' 手机号为空 '''
        response = self.client.post('/sign_index_action/7/', {"phone" : ""})
        # print("开始执行空手机号签到的用例...")
        # print(response)
        # print("打印服务器返回的页面")
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'phone error.', response.content)

    def test_sign_index_action_phone_or_event_id_error(self):
        ''' 手机号或发布会id错误 '''
        response = self.client.post('/sign_index_action/7/', phone = "13913301322")
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'phone error.', response.content)

    def test_sign_index_action_user_sign_has(self):
        ''' 执行用户已签到用例 '''
        response = self.client.post('/sign_index_action/7/', phone = "16666666666")
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'user has sign in.', response.content)

    def test_sign_index_action_sign_success(self):
        ''' 执行签到成功用例 '''
        response = self.client.post('/sign_index_action/3/', {'phone' : '13913301322'})
        # print(response)
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"sign in success!", response.content)





'''
运行所有用例：
python3 manage.py test

运行sign应用下的所有用例：
python3 manage.py test sign

运行sign应用下的tests.py文件用例：
python3 manage.py test sign.tests

运行sign应用下的tests.py文件中的 GuestManageTest 测试类：
python3 manage.py test sign.tests.GuestManageTest

......


'''