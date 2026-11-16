*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  hiisi
    Set Password  hiisi12345
    Confirm Password  hiisi1245
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  h
    Set Password  hiisi12345
    Confirm Password  hiisi1245
    Click  button >> text=Register
    Usermame Or Password Too Short


Register With Valid Username And Too Short Password
    Set Username  hiisi12345
    Set Password  h
    Confirm Password  h
    Click  button >> text=Register
    Usermame Or Password Too Short

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  6666666666666666666
    Confirm Password  6666666666666666666
    Click  button >> text=Register
    Get Text  body  *=  User with username kalle already exists

*** Keywords ***

Register Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password 
    [Arguments]  ${password}
    Fill Text  id=password  ${password}

Confirm Password 
    [Arguments]  ${password}
    Fill Text  id=password_confirmation  ${password}

Usermame Or Password Too Short
    Get Text  body  *=  Username must be at least 3 letters and password at least 8 letters long

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page