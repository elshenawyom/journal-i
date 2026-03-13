@echo off
cd /d "c:\Users\Work\Desktop\learning\year 3\undergrad seminar\journal-i"

python "c:\Users\Work\Desktop\learning\year 3\undergrad seminar\journal-i\journal_setup.py"
if %ERRORLEVEL% EQU 0 goto done

py "c:\Users\Work\Desktop\learning\year 3\undergrad seminar\journal-i\journal_setup.py"
if %ERRORLEVEL% EQU 0 goto done

echo Python not found via 'python' or 'py'. Trying full paths...
for /f "delims=" %%P in ('dir /b /s "C:\Python*\python.exe" 2^>nul') do (
    "%%P" "c:\Users\Work\Desktop\learning\year 3\undergrad seminar\journal-i\journal_setup.py"
    if !ERRORLEVEL! EQU 0 goto done
)

echo ERROR: Could not run Python.
exit /b 1

:done
echo Batch complete.
