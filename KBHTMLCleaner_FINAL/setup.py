from cx_Freeze import setup, Executable

setup(
    name = "KB HTML Cleaner", 
    version = "1.0", 
    description = "Cleans and organizes KB HTML Code", 
    executables = [Executable("KB_HTML_Cleaner.py")]
    )
