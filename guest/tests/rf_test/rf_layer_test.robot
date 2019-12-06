*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary


*** Variables ***
${URL}            https://www.baidu.com
${BROWSER}        Chrome


*** Test Cases ***
case1
    Open Browser    ${URL}    ${BROWSER}
    ${title}    Baidu Search    robot framework
    should contain    ${title}    robot framework_百度搜索
    close browser

case2
    Open Browser    ${URL}    ${BROWSER}
    ${title}    Baidu Search    selenium
    should contain    ${title}    selenium_百度搜索
    close browser


*** Keywords ***
Baidu Search
    [Arguments]    ${search_key}
    Input text    id:kw    ${search_key}
    click button    id:su
    Evaluate    time.sleep(2)    time
    ${title}    Get Title
    [Return]    ${title}