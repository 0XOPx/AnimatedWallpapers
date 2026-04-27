@echo off
title Wallpaper EXE Builder
echo [1/3] Cleaning up old builds...
if exist "dist" rd /s /q "dist"
if exist "build" rd /s /q "build"

echo [2/3] Building Wallpaper.exe...
:: Fixed filename to wallpaper.py and added the icon
pyinstaller --noconsole --onedir --noconfirm --clean ^
    --icon="Logo.ico" ^
    --collect-all cv2 ^
    --collect-all pygame ^
    "wallpaper.py"

echo [3/3] Finalizing assets...
:: Creating the folder first to make sure the copy works
if not exist "dist\wallpaper" mkdir "dist\wallpaper"
copy "video.mp4" "dist\wallpaper\video.mp4"

echo.
echo Done! Your EXE is in: C:\Users\natal\Desktop\Documents\Tapeta\dist\wallpaper\
pause