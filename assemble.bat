::if not exist .\bin\builder.exe (
::	.\install.bat
::)
::.\bin\builder.exe .\doc .\ME-Project.docx
.\builder\src\builder.py .\doc .\ME-Project.docx
