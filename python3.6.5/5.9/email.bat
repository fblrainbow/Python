@echo off
REM ��֤�����Ļ���
chcp 936
REM �������ӵ��ƻ�����Ϊ���ܽ��뵽ָ��·��
cd /d d:\SVN\Python\trunk\python3.6.5\5.9
REM ��֤�Ѿ�����������
:main
echo %date%-%time% >>test.txt
ping 8.8.8.8 -n 3 >>test.txt
find /i "��ʧ = 0" test.txt
REM �������ɹ�������������绷����ֱ�������ȶ�
if %ERRORLEVEL% EQU 1 goto main
python email1.py