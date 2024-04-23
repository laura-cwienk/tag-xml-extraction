# Use Command Prompt instead of sh:
set shell := ["cmd.exe", "/c"]

# Download and extract WinPython files
wp-pull:
  curl -LJO https://github.com/winpython/winpython/releases/download/7.5.20240410/Winpython64-3.12.3.0dotrc.exe
  Winpython64-3.12.3.0dotrc.exe -o ".\" -y
  del Winpython64-3.12.3.0dotrc.exe

# Copy compilation commands to clipboard
wp-clip:
  echo cd .. >> compile
  echo cd .. >> compile
  echo pip install pyinstaller >> compile
  echo pyinstaller -F xmltags.py >> compile
  echo move .\dist\xmltags.exe .\ >> compile
  echo rmdir /s /q .\dist >> compile
  echo rmdir /s /q .\build >> compile
  clip < compile
  del compile

# Start WinPython Command Prompt binary
wp-cmd:
  cd WPy64-31230
  start "WinPython Command Prompt.exe"

# Run wp-pull, wp-clip and wp-cmd recipes
wp-init:
  just -f {{justfile()}} wp-pull
  just -f {{justfile()}} wp-clip
  just -f {{justfile()}} wp-cmd
