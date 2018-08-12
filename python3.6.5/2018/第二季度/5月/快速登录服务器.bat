@echo off
setlocal enabledelayedexpansion
for /F "eol=; tokens=1,2 delims==" %%i in (config.ini) do (
	if %%i==IP set IP=%%j
	if %%i==Account set Account=%%j
	if %%i==Password set Password=%%j
)
set string=%Account%@%IP% -pw %Password%
start putty %string%
