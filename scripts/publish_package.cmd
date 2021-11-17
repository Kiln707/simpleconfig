CWD=%~dp0
cd ..
twine upload dist\*
cd %CWD%
pause
