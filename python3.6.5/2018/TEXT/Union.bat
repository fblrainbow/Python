@echo off
setlocal enabledelayedexpansion
if exist ���ƾ���.txt del ���ƾ���.txt
for /f %%i in ('dir /o:d /b *.txt') do (
type %%i >>���ƾ���.txt
)
