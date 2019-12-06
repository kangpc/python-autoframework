from django.contrib import admin
from sign.models import Event, Guest

# Register your models here.
# Django自带的admin后台，把models里面数据库的表映射到后台进行管理。
# 1 创建发布会
# 在admin的发布会列表显示更多字段
class EventAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ['name', 'limit', 'status', 'address', 'start_time', 'id']
    search_fields = ['name']  #搜索栏
    list_filter = ['status']  #过滤器

class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone','email','sign','create_time','event']
    search_fields = ['realname','phone'] #搜索栏
    list_filter = ['sign']  #过滤器

# 把表Event, Guest注册到后台
admin.site.register(Event, EventAdmin)
admin.site.register(Guest)



