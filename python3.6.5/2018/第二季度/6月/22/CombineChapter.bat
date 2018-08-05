@echo off
rem chcp 65001
setlocal enabledelayedexpansion
cd %cd%\%1\%2
rem echo %cd%
rem if exit %3.txt del %3.txt  "usebackq delims=="
for /f %%i in ('dir /o:d /b *.txt') do (
	echo %%i
	type %%i >> %3.txt
	)