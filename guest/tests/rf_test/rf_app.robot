*** Settings ***
Library           AppiumLibrary

*** Test Cases ***
case1
    [Documentation]    Test open app
    Open Application    http://localhost:4723/wd/hub    platformName=Android    platformVersion=8.1    deviceName=0123456789ABCDEF    appPackage=com.example.android.contactmanager    appActivity=com.example.android.contactmanager.ContactManager

# case2
#     [Documentation]    Test addition
#     Click Element    com.android.calculator2:id/digit_9                          # 点击数字 9
#     Click Element    accessibility_id=plus                                       # 点击 + 号
#     Click Element    xpath=//android.widget.Button[contains(@text,'7')]          # 点击数字 7
#     Click Element    android=new UiSelector().description(\"equals\")            # 点击 = 号
#     ${actual_text}   Get Text    com.android.calculator2:id/result               # 获取计算结果
#     Should Be Equal As Strings    ${actual_text}    16                           # 验证结果等于16
#     sleep    2                                                                   # 设置等待2S
#     Click Element    com.android.calculator2:id/clr                              # 点击清除键

# case3
#     [Documentation]    Test subtraction
#     Click Element    com.android.calculator2:id/digit_8                          # 点击数字 8
#     Click Element    accessibility_id=minus                                      # 点击 - 号
#     Click Element    xpath=//android.widget.Button[contains(@text,'2')]          # 点击数字 2
#     Click Element    accessibility_id=equals                                     # 点击 = 号
#     Click Element    com.android.calculator2:id/clr                              # 点击清除键

# case4
#     [Documentation]    Test close app
#     Click Element    accessibility_id=More options                               # 点击更多选项
#     Click Element    xpath=//android.widget.TextView[contains(@text,'Open source licenses')]
#     sleep    5                                                                   # 设置等待5S
#     Press Keycode    4                                                           # 模拟返回键
#     Close Application                                                            # 关闭当前应用

