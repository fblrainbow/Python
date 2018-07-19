@echo off
setlocal enabledelayedexpansion
if exist ╩Йфф╬елЛ.txt del ╩Йфф╬елЛ.txt
for /f %%i in ('dir /o:d /b *.txt') do (
type %%i >>╩Йфф╬елЛ.txt
)
