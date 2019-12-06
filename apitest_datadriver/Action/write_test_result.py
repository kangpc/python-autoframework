# encoding:utf-8

from Config.public_data import *


def write_result(wbObj, sheetObj, responseData, errorKey, rowNum):
    try:
        # 写响应body
        wbObj.writeCell(sheet=sheetObj, content="%s" % responseData,
                        rowNo=rowNum, colsNo=CASE_responseData)
        # 写校验结果状态列及错误信息列
        if errorKey:  # errorKey为空，执行成功，只写状态;非空，执行失败，写状态，写错误信息。
            wbObj.writeCell(sheet=sheetObj, content="faild", rowNo=rowNum, colsNo=CASE_status)
            wbObj.writeCell(sheet=sheetObj, content="%s" % errorKey, rowNo=rowNum, colsNo=CASE_errorInfo)
        else:
            wbObj.writeCell(sheet=sheetObj, content="pass", rowNo=rowNum, colsNo=CASE_status)
    except Exception, e:
        raise e

if __name__ == '__main__':
    write_result()

