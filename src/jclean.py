from sys import argv
from os import remove, getcwd, listdir
from time import time
from JPack.print_args import default, jclean_print_args
from JPack.args import jclean_args
from JPack.file_sys import get_embeded_files

__version__ = "1.1.0.0"

def main():
    global __START__
    __START__ = time()

    if len(argv) == 1:
        print(default.NO_ARG)
        return

    _self = argv.pop(0)

    for arg in argv:
        if jclean_args.help(arg):
            jclean_print_args.help()
            return
        elif jclean_args.version(arg):
            jclean_print_args.version(__version__)
            return
        elif jclean_args.equAll(arg):
            all()
            return
        elif jclean_args.equfile(argv[0]):
            spec_file(argv[0])
            return
        else:
            print(f"{_self} - Invalid argument: {arg}")
            return

def all():
    wd = getcwd()

    correct_check = listdir(wd)
    hasMain = [item for item in correct_check if item.endswith(".java")]

    if hasMain.__contains__("Main.java") is False: 
        print("Please use commands in the directory that contains your 'Main.java' file")
        return

    ls = get_embeded_files(wd)
    cfiles = [lsi for lsi in ls if lsi.endswith(".class")]
    for cfile in cfiles:
        remove(cfile)
        print(f"File removed: {cfile}")

    print("Cleanup finished")
    print(f"Elapsed time: {(time() - __START__):.2f}")
    
def spec_file(file: str):
    wd    = getcwd()
    _file = 0x000000

    cfiles = get_embeded_files(wd)


    for cfile in cfiles:
        if cfile.endswith(file):
            _file = cfile

    if _file == 0x000000:
        print(f"File not found:{file}")
        return

    remove(f"{_file}")
    print(f"File removed: {_file}")

if __name__ == "__main__":
    main()