from django.db import models

# Create your models here.

# ORM   -->用编程语言的语法来操作数据库，而不是sql语句

# django集成了ORM，也可以单独拿ORM出来用
'''
创建和管理数据库表的文件
  --编程语言  --- ORM ---> 数据库驱动（pymysql）  --- 数据库

# Read a single record
sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
cursor.execute(sql, ('webmaster@python.org',))  --执行sql，然后把'webmaster@python.org'传给email
result = cursor.fetchone()

在ORM里不能直接写sql
sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
cursor.execute(sql, ('webmaster@python.org',))
上面两行在ORM里是这样写的,比较接近编程语言,
user1 = User.objects.get('email'='webmaster@python.org')
user1.id    --就是sql里的select id
user1.password


sql = "select * from table"
pymysql.run(sql)

设计系统表
Django 提供完善的模型(model)层主要用来创建和存取数据，不需要我们直接对数据库操作。
Django 模型基础知识:
每个模型是一个 Python 类,继承 django.db.models.model 类.
该模型的每个属性表示一个数据库表字段.
所有这一切,已经给你一个自动生成的数据库访问的 API.
打开.../sign/models.py 文件,完成表的创建.

    发布会签到系统,比如小米发布会

    发布会管理表:  --创建发布会表结构:
    id(自增,主键) int,
    发布会名称 char 必填,
    发布会时间 datetime 必填,
    地址 char 必填,
    场地容纳参加人数 int 必填,
    状态(1未开始/开启,0已过期/关闭) tinyint 选填,
    创建时间 (自动获取当前时间) datetime

    嘉宾表:  --(媒体,米粉,厂商(下游[自媒体] 下游[高通芯片])
    姓名 char 必填,
    手机号(唯一) varchar 必填,
    邮箱(django有专门的类型) varchar,
    发布会id int 必填,
    状态(1已签到,0未签到),
    签到时间 datetime
      --手机号+发布会做联合主键
      一个嘉宾一定要所属于某一场发布会
      一个嘉宾可以参加多场发布会
      一个发布会只能有一个同名的嘉宾

    写sql语句


'''
#ORM
#以对象方式来建表（Event），就是一个class，继承django里的models.Model类
class Event(models.Model):
    ''' 发布会表 '''
    name = models.CharField(max_length=100)            # 发布会标题
    limit = models.IntegerField()                      # 参加人数
    status = models.BooleanField()                     # 状态（0关闭，1开启）
    address = models.CharField(max_length=200)         # 地址
    start_time = models.DateTimeField('events time')                # 发布会时间
    create_time = models.DateTimeField(auto_now=True)  # 创建时间(自动获取当前时间)

    # 把发布会对象（Event object (1)）标识显示为我们自己定义的字段
    def __str__(self):
        return self.name

class Guest(models.Model):
    ''' 嘉宾表 '''
    # on_delete，删除A数据时，把关联表的A也删除
    event = models.ForeignKey(Event, on_delete=models.CASCADE) # 关联发布会 id
    realname = models.CharField(max_length=64)                 # 姓名
    phone = models.CharField(max_length=16)                    # 手机号
    email = models.EmailField()                                # 邮箱
    sign = models.BooleanField()                               # 签到状态
    create_time = models.DateTimeField(auto_now=True)          # 创建时间（自动获取当前时间）

    class Meta:
        unique_together = ("phone", "event")
        ordering = ['-id']
        ''' ordering = ['-id'] 去除警告：UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list
'''
    def __str__(self):
        return self.realname


# 修改创建时间类型
# ALTER TABLE  `sign_event` CHANGE  `create_time`  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
# ALTER TABLE  `sign_guest` CHANGE  `create_time`  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
