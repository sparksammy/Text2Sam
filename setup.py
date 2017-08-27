from cx_Freeze import setup, Executable
 
setup(
    name = "txt2sparksammy",
    version = "0.1",
    description = "Text to Sparksammy Talk",
    executables = [Executable("load.py")]
    )