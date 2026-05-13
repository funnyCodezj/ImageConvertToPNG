@echo off
chcp 65001 >nul
echo ========================================
echo   ImageConvertToPNG - Build EXE
echo ========================================
echo.

pyinstaller --noconfirm --clean ImageConvertToPNG.spec

echo.
if %ERRORLEVEL%==0 (
    echo ========================================
    echo  Build successful!
    echo  Output: dist\ImageConvertToPNG\
    echo  Run:    dist\ImageConvertToPNG\ImageConvertToPNG.exe
    echo ========================================
) else (
    echo ========================================
    echo  Build failed. Check error messages above.
    echo ========================================
)
pause
