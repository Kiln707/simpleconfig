CWD=%~dp0
cd ..
python -m setup.py build_sphinx
cd %CWD%
pause
