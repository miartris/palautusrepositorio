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

Register Rejects Lowercase Letters Only Password
    Set Username  loweruser
    Set Password  passwordonly
    Confirm Password  passwordonly
    Click  button >> text=Register
    Password Must Include Number Or Special Character

Register Rejects Uppercase Letters Only Password
    Set Username  upperuser
    Set Password  PASSWORDONLY
    Confirm Password  PASSWORDONLY
    Click  button >> text=Register
    Password Must Include Number Or Special Character

Register Rejects Mixed Case Letters Only Password
    Set Username  mixeduser
    Set Password  PasswordOnly
    Confirm Password  PasswordOnly
    Click  button >> text=Register
    Password Must Include Number Or Special Character

Register Accepts Password With Special Character
    Set Username  specialuser
    Set Password  Password!
    Confirm Password  Password!
    Click  button >> text=Register
    Register Should Succeed

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

Password Must Include Number Or Special Character
    Get Text  body  *=  Password must include at least one number or special character

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page