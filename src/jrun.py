from JPack.console import CmdLine
from JPack.args import jrun_args
from JPack.print_args import jrun_print_args
from sys import argv
from os import listdir, getcwd
from time import time

__version__ = "1.0.0.0"

__START__ = time()

def main():
    if len(argv) == 1:
        main_jav()
        return

    argv.remove(argv[0])

    for arg in argv:
        if jrun_args.help(arg):
            jrun_print_args.help()
            return
        elif jrun_args.version(arg):
            jrun_print_args.version(__version__)
            return
        if jrun_args.mainfile(arg):
            main_jav()
            return
        else:
            spec_jav(argv[0])
            return

def main_jav():
    wd = getcwd()
    mainfile = "Main"

    cfiles = listdir(wd)

    if not cfiles.__contains__("Main.class"):
        print("Main.class not found")
        return

    print("\n")
    CmdLine(wd).run(f"{mainfile}")

    print("Program Terminated")
    print(f"Elapsed time: {(time() - __START__):.2f}")

def spec_jav(file: str):
    wd = getcwd()

    _files = listdir(wd)
    files = []

    for _file in _files:
        if _file.endswith(".class"):
            files.append(_file)

    hasFile = files.__contains__(f"{file}.class")

    if hasFile:
        CmdLine(wd).run(file)
    else:
        print(f"File: {file}.class does not exist")
        print(f"if the file is {file}.java")
        print(f"Run 'jcompile {file}.java' or 'jcompile all'")


    print("Program terminated")
    print(f"Time elapsed: {(time() - __START__):.2f}")

if __name__ == "__main__":
    main()