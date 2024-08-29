@echo off
echo Creating virtual environment...
python -m venv .venv

echo Activating virtual environment...
call .venv\Scripts\activate

echo Installing dependencies...
pip install -r .\assets\requirements.txt

:: Ejecutar el script test.py
python .\run.py

:: Desactivar el entorno virtual
deactivate

:: Indicar que el entorno virtual está activo
echo El entorno virtual ha sido creado, las dependencias han sido instaladas y el script test.py ha sido ejecutado.

:: Mantener la ventana abierta
pause