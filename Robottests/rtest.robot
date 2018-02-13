*** Settings ***
Library    Selenium2Library

*** Variables ***
${ROOT}     http://www.dcu.org
${BROWSER}  chrome


*** Test Cases ***
Login of an existing customer
    [Setup]     Open a browser to Super Website 2000!
    [Teardown]  Close all browsers

    Enter a valid username
    Enter a valid password
    click button  id=submitBtn


Open Close Browser Again
    Open browser   http://bbcnews.com  ${BROWSER}
    Close browser


*** Keywords ***
Open a browser to Super Website 2000!
    # this is a pre-defined Selenium2Library keyword
    Open browser  ${ROOT}    ${BROWSER}
    sleep       20s

Enter a valid username
    # these are pre-defined Selenium2Library keywords
    wait until element is visible    id=userid
    input text    id=userid  5233108

Enter a valid password
    # these are pre-defined Selenium2Library keywords
    wait until element is visible      id=password
    input text    id=password    Thoku1234!