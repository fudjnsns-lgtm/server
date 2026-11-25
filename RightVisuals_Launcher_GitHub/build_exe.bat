@echo off
cd /d "%~dp0"
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py -m PyInstaller --noconfirm --clean --onefile --windowed --name RightVisualsLauncher main.py
echo.
echo EXE: dist\RightVisualsLauncher.exe
pause
