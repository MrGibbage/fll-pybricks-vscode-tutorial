@echo off
setlocal
color 07
echo Git pull in 5 seconds...
timeout /t 5 /nobreak
git pull
set "VAR_NAME=robotName"
if defined %VAR_NAME% (
    color 0A
    echo Your robot name is: %robotName%
) else (
    color 0C
    echo Your robotName environment variable has not been set
)
@echo off
color 0A
echo This text is green on a black background.
color 1E
echo This text is yellow on a blue background.
color 4F
echo This text is white on a red background.
echo.