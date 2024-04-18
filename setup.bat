@echo off
curl -LJO https://github.com/winpython/winpython/releases/download/7.5.20240410/Winpython64-3.12.3.0dotrc.exe
Winpython64-3.12.3.0dotrc.exe -o ".\" -y
del Winpython64-3.12.3.0dotrc.exe
echo cd .. >> compile
echo cd .. >> compile
echo pip install pyinstaller >> compile
echo pyinstaller -F mainapp.py >> compile
echo move .\dist\mainapp.exe .\ >> compile
echo rmdir /s /q .\dist >> compile
echo rmdir /s /q .\build >> compile
clip < compile
del compile
cd WPy64-31230
start "WinPython Command Prompt.exe"
