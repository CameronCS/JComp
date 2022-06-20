from os import getcwd, listdir
from time import time
from sys import argv
from JPack.args import jcompile_args
from JPack.file_sys import get_embeded_files, get_folder, get_file
from JPack.print_args import default, jcompile_print_args
from JPack.console import CmdLine

__version__ = "1.1.0.1"

def main():
    global __START__
    __START__ = time()

    if len(argv) == 1:
        print(default.NO_ARG)
        return

    _self = argv.pop(0)

    for arg in argv:
        if jcompile_args.help(arg):
            jcompile_print_args.help()
            return
        elif jcompile_args.version(arg):
            jcompile_print_args().version(__version__)
            return
        elif jcompile_args.all(arg):
            all()
            return
        elif jcompile_args.equFile(arg):
            comp_file(arg)
            return
        else: 
            print(f"{_self} - Invalid argument: {arg}")
            return

def all():
    wd = getcwd()
    ls = get_embeded_files(wd)
    fc = 0

    jcheck = listdir(wd)
    if jcheck.__contains__("Main.java") is False:
        print("Please use this command in the directory that contains the 'Main.java' file")
        return


    jembeds = [lsi for lsi in ls if lsi.endswith(".java")]
    max_index = len(jembeds)

    print("Compile all Started")

    jfiles   = []
    jfolders = []
    for jembed in jembeds:
        jfiles.append(get_file(jembed))
        jfolders.append(get_folder(jembed))
    
    for i in range(max_index):
        exitcode = CmdLine(jfolders[i]).compile(jfiles[i])
        if exitcode.value > 0:
            print(f"Error in file: {jfiles[i]}")
            print("Compile stopped")
        else:
            fc += 1

    print("Compile all finished")
    print(f"{fc}: Files compiled")
    print(f"Elapsed time {(time() - __START__):.2f}")

def comp_file(arg: str):
    print(f"Compiling {arg} and all related files")

    wd = getcwd()
    _files = get_embeded_files(wd)

    folders = []
    files = []

    for _file in _files:
        files.append(get_file(_file))
        folders.append(get_folder(_file))

    if not arg in files:
        print(f"File: {arg} was not found")
        print("Compile failed")
        return

    index = files.index(arg)
    folder = folders[index]
    exitcode = CmdLine(folder).compile(arg)
    if exitcode.value > 0:
        print(f"File: {arg} could not be compiled due to an error")
        print(f"in file {arg} or related file")
        return

    print(f"File: {arg} and all related files compiled")
    print(f"Time elapsed: {(time() - __START__):.2f}")

if __name__ == "__main__":
    main()