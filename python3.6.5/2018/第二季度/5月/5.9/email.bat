@echo off
REM 保证是中文环境
chcp 936
REM 后面会添加到计划任务，为了能进入到指定路径
cd /d d:\SVN\Python\trunk\python3.6.5\5.9
REM 保证已经连上网络了
:main
echo %date%-%time% >>test.txt
ping 8.8.8.8 -n 3 >>test.txt
find /i "丢失 = 0" test.txt
REM 联网不成功则继续监视网络环境，直到网络稳定
if %ERRORLEVEL% EQU 1 goto main
python email1.py