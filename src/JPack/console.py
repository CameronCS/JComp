from os import system

__package__ = "JPack"
__version__ = "1.1.0.0"
__name__    = "console_instance.py"
__all__     = [
    "ExitCode",
    "CmdLine"
]

class ExitCode:
    value = 0
    def __init__(self, value: int) -> None:
        self.value = value
    def __repr__(self) -> str:
        return f"System exit code: {self.value}"

class CmdLine:
    def __init__(self, path: str) -> None:
        self.path = path

    def _compile(self, file: str) -> ExitCode:
        exitcode = ExitCode(system(f"cd {self.path} & javac {file}"))
        if exitcode.value > 0:
            print(f"Error in file: {file} or related file")
            print("Compile Stopped")
            return exitcode
        else:
            print(f"File Compiled: {file}")
            return ExitCode(0)

    def compile(self, files: list[str] | str) -> ExitCode:
        if isinstance(files, str) is True: return self._compile(files) 
        else: _last_index = len(files) - 1

        for file in files:
            exitcode = self._compile(file)
            if exitcode.value != 0 and file != files[_last_index]: return exitcode
            elif file == files[_last_index]: return ExitCode(0)

    def run(self, file: str) -> ExitCode:
        if file.endswith(".java"): file = file.removesuffix(".java")
        exitcode = ExitCode(system(f"cd {self.path} & java {file}"))
        if exitcode.value > 0: 
            print(f"An Error occured when trying to run {file}")
            return exitcode
        else: return ExitCode(0)