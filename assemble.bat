::if not exist .\bin\builder.exe (
::	.\install.bat
::)
::.\bin\builder.exe .\doc .\ME-Project.docx
python3 .\builder\src\builder.py .\doc .\ME-Project.docx
