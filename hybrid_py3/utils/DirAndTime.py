#encoding=utf-8
import time, os
from datetime import datetime
from config.VarConfig import screenPicturesDir

# 获取当前的日期
def getCurrentDate():
    timeTup = time.localtime()
    currentDate = str(timeTup.tm_year) + "-" + \
        str(timeTup.tm_mon) + "-" + str(timeTup.tm_mday)
    return currentDate

# 获取当前的时间
def getCurrentTime():
    timeStr = datetime.now()
    nowTime = timeStr.strftime('%H-%M-%S-%f')
    return nowTime

# 创建截图存放的目录
def createCurrentDateDir():
    dirName = os.path.join(screenPicturesDir, getCurrentDate())
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    return dirName

if __name__ == '__main__':
    print(getCurrentDate())
    print(createCurrentDateDir())
    print(getCurrentTime())
