# Imports
from sys import argv
from JPack.create_java_app import make, makedir, makedirs, makefile, makefiles
from JPack.print_args import default, jcomp_print_args
from JPack.args import jcomp_args

__version__ = "1.1.0.0"

def main():
    if len(argv) == 1:
        print(default.NO_ARG)
        return

    _self = argv.pop(0)

    for arg in argv:
        if jcomp_args.equHelp(arg):
            jcomp_print_args.help() 
            return
        elif jcomp_args.equVer(arg):
            jcomp_print_args.version(__version__)
            return
        elif jcomp_args.equCJA(arg):
            makeargs = argv
            makeargs.remove(makeargs[0])
            if len(makeargs) == 0:
                makeargs.append("my-java-app")
            make(makeargs)
            return
        elif jcomp_args.equAF(arg):
            makefile(argv[1])
            return
        elif jcomp_args.equAD(arg):
            makedir(argv[1])
            return
        elif jcomp_args.equAFS(arg):
            args = argv
            args.remove(args[0])
            makefiles(args)
            return
        elif jcomp_args.equADS(arg):
            args = argv
            args.remove(args[0])
            makedirs(args)
            return
        else:
            print(f"{_self} - Invalid arg: {arg}")
            return

if __name__ == "__main__":
    main()