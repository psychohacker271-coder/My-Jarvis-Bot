@echo off
setlocal
cd /d "%~dp0"

if not exist "nexora_local_brain.py" (
  echo Missing nexora_local_brain.py. Download the GitHub setup files into this folder first.
  pause
  exit /b 1
)

set "OLLAMA_EXE="
for /f "delims=" %%I in ('where ollama 2^>nul') do if not defined OLLAMA_EXE set "OLLAMA_EXE=%%I"
if not defined OLLAMA_EXE if exist "%LOCALAPPDATA%\Programs\Ollama\ollama.exe" set "OLLAMA_EXE=%LOCALAPPDATA%\Programs\Ollama\ollama.exe"

if not defined OLLAMA_EXE (
  echo Ollama was not found. Install and open Ollama, then run this file again.
  pause
  exit /b 1
)

powershell -NoProfile -Command "try { Invoke-RestMethod 'http://127.0.0.1:11434/api/tags' -TimeoutSec 2 | Out-Null; exit 0 } catch { exit 1 }"
if errorlevel 1 (
  echo Starting Ollama...
  start "" /B "%OLLAMA_EXE%" serve
  set /a tries=0
  :waitollama
  timeout /t 2 /nobreak >nul
  powershell -NoProfile -Command "try { Invoke-RestMethod 'http://127.0.0.1:11434/api/tags' -TimeoutSec 2 | Out-Null; exit 0 } catch { exit 1 }"
  if errorlevel 1 (
    set /a tries+=1
    if %tries% GEQ 10 (
      echo Ollama did not start. Open Ollama manually and try again.
      pause
      exit /b 1
    )
    goto waitollama
  )
)

echo Installing or checking NEXORA Local Brain dependencies...
py -m pip install -r requirements-local-brain.txt
if errorlevel 1 (
  echo Dependency installation failed. Check Python and internet access.
  pause
  exit /b 1
)

echo.
echo Starting NEXORA Local Brain. Keep this window open.
py nexora_local_brain.py
pause
