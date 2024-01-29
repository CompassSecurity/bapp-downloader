@echo off

echo.
echo Command to install the requirements: python3 -m pip install -r requirements.txt
echo.
::Execute virtual python env
::.\venv\Scripts\activate

::Downlaod extensions
python3 bapp_downloader.py

::Move the extensions to other location
move bapps\* ..\Burp_Extensions\

echo.
echo Task compelted. Compress the files more than 50MB.
echo.
pause
