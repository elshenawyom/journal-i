@echo off
mkdir "%~dp0.vscode"
move /Y "%~dp0launch.json" "%~dp0.vscode\launch.json"
echo Installed .vscode\launch.json
pause
