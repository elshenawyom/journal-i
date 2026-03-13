@echo off
echo ========================================
echo  Constructor Mathematics Review Setup
echo ========================================
echo.

cd /d "%~dp0"

echo [1/3] Running file organisation...
python journal_setup.py
if errorlevel 1 (
    echo.
    echo ERROR: Python script failed. Check output above.
    echo Make sure Python is installed and accessible.
    pause
    exit /b 1
)

echo.
echo [2/3] Compilation complete. See main.pdf.
echo.
echo ========================================
echo  Done! Open main.pdf to view the journal
echo ========================================
pause
