@echo off
cd /d D:\SVN\Python\trunk\python3.6.5\5.9\python发邮件\
cd /d d:\SVN\Python\trunk\python3.6.5\5.9\python发邮件


:
ping 47.91.232.233 -n 3 >test.txt
for /f "skip=8 takens=2,* delims== " %%i in (test.txt) do @echo %%i