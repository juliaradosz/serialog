@echo off
rem Uruchamia SeriaLog z kontami użytkowników i otwiera przeglądarkę.
cd /d "%~dp0"
start "" http://localhost:8000
python server.py
pause
