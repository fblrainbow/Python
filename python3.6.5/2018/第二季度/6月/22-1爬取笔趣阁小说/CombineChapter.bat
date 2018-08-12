@echo off
rem chcp 65001
setlocal enabledelayedexpansion
rem move /y *.txt %cd%\%1\%2 
cd %cd%\%1\%2
rem echo %cd%
rem if exit %3.txt del %3.txt
for /f %%i in ('dir /o:d /b *.txt') do (
	echo %%i
	type %%i >> %3.txt
	)