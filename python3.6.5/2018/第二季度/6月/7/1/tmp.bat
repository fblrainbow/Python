@echo off
:a
tasklist /FI "IMAGENAME EQ python.exe" > tmp.txt
findstr "python.exe" tmp.txt
REM if not %errorlevel%==0 (
python.exe 1.py
REM )
ping 127.0.0.1 -n 50
goto a