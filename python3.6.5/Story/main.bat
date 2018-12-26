@echo off
cd /d F:\SVN\Python\trunk\python3.6.5\Story
echo %CD%
ECHO %CD% >>TMP.LOG
DEL ÖÁ×ðÐÞÂÞ.txt
ping 127.0.0.1 -n 5 >nul

python main.py

ping 127.0.0.1 -n 5 >nul