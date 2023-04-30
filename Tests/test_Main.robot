*** Settings ***
Library    Process
Library    ../settings.py


*** Variables ***
${path}    ../
${python310}    C:\\Python310\\python.exe

*** Test Cases ***
After starting main app as python script, it keeps running in the background
    Start main application using python script
#    Wait a moment
    Check if database file exists
#    Wait a moment
    Check connection to database
#    Wait a moment
    Main application should be running
#    Wait a moment
    Close process

*** Keywords ***
Start main application using python script
    ${process}=    Start process    ${python310}    main.py
    ${processid}=  Get Process ID
	Log To Console  ${processid}

Wait a moment
    BuiltIn.Sleep    1s

Main application should be running
	${running}=  Is process running
    Should be equal  ${running}  ${True}  msg=APP is not running, but should be

Check if database file exists
    ${dataexists}=    settings.database exist check
    should be equal    ${dataexists}    ${True}

Check connection to database
    settings.connect to database

Close process
   Terminate process    kill=True
