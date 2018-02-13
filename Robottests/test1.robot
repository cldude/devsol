*** Settings ***
#Documentation   read yaml
#Force Tags      read yaml
#Library    foundation/setupteardown/ClusterMaintenanceSetupTeardown.py
Library         rbtest
Library         String
Library        Collections
#Suite Setup    onboard cluster setup
#Suite Teardown    onboard cluster teardown


*** Variables ***
${user}                "Harsha"



*** Test Cases ***
sample test case
   test1

For-Loop-In-Range
     : FOR    ${INDEX}    IN RANGE    1    3
     \    Log    ${INDEX}
     \    ${RANDOM_STRING}=    Generate Random String    ${INDEX}
     \    Log    ${RANDOM_STRING}

For-Loop-Elements
    @{ITEMS}    Create List    Star Trek    Star Wars    Perry Rhodan
    :FOR    ${ELEMENT}    IN    @{ITEMS}
    \    Log    ${ELEMENT}
    \    ${ELEMENT}    Replace String    ${ELEMENT}    ${SPACE}    ${EMPTY}
    \    Log    ${ELEMENT}

For-Loop-Exiting
    @{ITEMS}    Create List    Good Element 1    Break On Me    Good Element 2
    :FOR    ${ELEMENT}    IN    @{ITEMS}
    \    Log    ${ELEMENT}
    \    Run Keyword If    '${ELEMENT}' == 'Break On Me'    Exit For Loop
    \    Log    Do more actions here ...
Repeat-Action
    Repeat Keyword    2    Log    Repeating this ...


Run-Keyword
        ${MY_KEYWORD}=    Set Variable    Log
        Run Keyword    ${MY_KEYWORD}    Test

Run-Keyword-If
        ${TYPE}=    Set Variable    V1
        Run Keyword If    '${TYPE}' == 'V1'    Log     Testing Variant 1
        Run Keyword If    '${TYPE}' == 'V2'    Log    Testing Variant 2
        Run Keyword If    '${TYPE}' == 'V3'    Log    Testing Variant 3

Run-Keyword-Ignore-Error
        @{CAPTAINS}    Create List    Picard    Kirk    Archer
        Run Keyword And Ignore Error    Should Be Empty    ${CAPTAINS}
        Log    Reached this point despite of error

StringsAndLists
      ${SOME_VALUE}=    Set Variable    "Test Value"
      Log    ${SOME_VALUE}
      @{WORDS}=    Split String    ${SOME_VALUE}    ${SPACE}
      ${FIRST}=    Get From List    ${WORDS}    0
      Log    ${FIRST}





*** Keywords ***
test1
   hello         ${user}

