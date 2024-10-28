@echo off
echo Building Daily Driver...

:: Create dist directory if it doesn't exist
if not exist "dist" mkdir dist

:: Clean previous builds
rmdir /s /q "build" 2>nul
rmdir /s /q "dist" 2>nul

:: Build executable using PyInstaller
pyinstaller --clean ^
    --name "DailyDriver" ^
    --icon "src\resources\icon.ico" ^
    --add-data "src\resources\white_rabbit.ttf;resources" ^
    --add-data "src\resources\icon.ico;resources" ^
    --add-data "src\tasks.json;." ^
    --noconsole ^
    --onefile ^
    src\main.py

echo Build complete!