*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${url}    http://127.0.0.1:8000/api

*** Test Cases ***
test_get_event_list
    Comment    查询发布会（get请求）
    ${payload}=    create dictionary    eid=3
    Create Session    alias=event    url=${url}
    ${r}=    Get Request    event    /get_event_list/    params=${payload}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}   message
    Should Be Equal    ${msg}    success.
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(200)
    Should Be Equal    ${sta}    ${status}


test_add_event
    Comment    添加发发布会(post请求)
    Create Session    event    ${url}
    &{headers}    Create Dictionary    Content-Type=application/x-www-form-urlencoded    # post请求需要请求头
    &{payload}=    Create Dictionary    eid=7    name=华为7 发布会    limit=8000    status=1    address=鸟巢    start_time=2020-1-1 18:00:00
    ${r}=    Post Request    event    /add_event/    data=${payload}    headers=${headers}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}    message
    Should Be Equal    ${msg}    add event success.
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(200)
    Should Be Equal    ${sta}    ${status}
