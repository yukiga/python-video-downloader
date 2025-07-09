@echo off
cd /d "%~dp0"
echo Instalando dependencias...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo Dependencias instaladas correctamente.
pause
