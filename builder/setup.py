from cx_Freeze import setup, Executable
import sys

build_exe_options = {
    "includes": [
        "sys",
        "subprocess",
        "os",
        "docxcompose.composer",
        "docx",
        "docx2pdf",
        "pathlib"
    ],
    "excludes": [
        "tkinter",
	"PyQt4",
        "PyQt5",
        "Cython"
    ],
    "optimize": 2
}

setup(
    name = "builder",
    options = {"build_exe": build_exe_options},
    executables = [Executable("./src/builder.py", base=None)]
)
