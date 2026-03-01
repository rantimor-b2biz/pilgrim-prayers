@echo off
:: setup-auto-sync.bat
:: Registers the auto-sync script with Windows Task Scheduler
:: Run ONCE as Administrator — right-click → "Run as administrator"

set PROJECT_PATH=C:\Users\rant\Documents\ran-workspace\Pilgrim
set SCRIPT_PATH=%PROJECT_PATH%\T-tools\scripts\auto-sync.ps1
set TASK_NAME=PilgrimPrayers-GitSync

echo.
echo Setting up automatic GitHub sync for Pilgrim Prayers...
echo Project folder: %PROJECT_PATH%
echo.

:: Delete existing task if it exists
schtasks /delete /tn "%TASK_NAME%" /f >nul 2>&1

:: Create the scheduled task — runs every 5 minutes, starting at logon
schtasks /create ^
  /tn "%TASK_NAME%" ^
  /tr "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File \"%SCRIPT_PATH%\"" ^
  /sc MINUTE ^
  /mo 5 ^
  /ru "%USERNAME%" ^
  /it ^
  /f

if %ERRORLEVEL% EQU 0 (
    echo.
    echo SUCCESS! Auto-sync is now active.
    echo Your Pilgrim Prayers folder will sync with GitHub every 5 minutes.
    echo.
    echo To check sync log: open T-tools\scripts\sync-log.txt
    echo To stop syncing:   schtasks /delete /tn "%TASK_NAME%" /f
) else (
    echo.
    echo ERROR: Could not create scheduled task.
    echo Make sure you ran this as Administrator.
)

echo.
pause
