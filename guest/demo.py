import time

# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
# print(time.strptime("2019-04-13 15:48:37","%Y-%m-%d %H:%M:%S"))

# a = []
# if not a:
#     print("列表a是空的")


# t = "2019-01-10 14:00:00"
# time_tuple = time.strptime(t, "%Y-%m-%d %H:%M:%S")
# print("-----------time_tuple: ", time_tuple)
# e_time = int(time.mktime(time_tuple))
# print("----- -----e_time: ", e_time)

# p = 'aaa'
# print(int(p))


# eid = '3'
# phone = '4'
# if eid == '' or phone == '':
#    print("lalala")

# if 0 is False:
#     print("0 is not False")


# '''当迭代的对象迭代完并为空时，位于else的子句将执行，而如果在for循环中含有break时则直接终止循环，
# 并不会执行else子句。
# '''
# a = 0
# b = 0
#
#
# for i in range(6):
#     if i == 5:
#         print('found it! i = %s' % i)
#         break
# else:
#     print('not found it ...')
import time
from selenium import webdriver
# chrome_user_data = r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default"
# option = webdriver.ChromeOptions()
# option.add_argument(chrome_user_data)
d = webdriver.Chrome()
d.get("http://www.baidu.com")


