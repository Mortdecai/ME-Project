mkdir .\bin

cxfreeze ./src/builder.py --target-dir ./bin
::pyinstaller -w -F ./src/builder.py
::pyinstaller ./src/builder.py

::move .\dist\builder.exe .\bin
::rd /s /q .\build .\dist .\src\__pycache__ 
::del /q .\builder.spec