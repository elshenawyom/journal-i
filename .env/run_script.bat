@echo off
cd /d "c:\Users\Work\Desktop\learning\year 3\undergrad seminar\journal-i"
python journal_setup.py
if errorlevel 1 (
    echo Python failed, trying py...
    py journal_setup.py
)
