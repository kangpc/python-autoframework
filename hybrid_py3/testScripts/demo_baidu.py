from action.PageAction import *
url="https://www.baidu.com/"
open_browser(chromeDriverFilePath)
visit_url(url)
input_string("id","kw","康平汆")
click("id","su")
close_browser()

