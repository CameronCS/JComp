from sys import argv
from time import time
from os import getcwd, listdir
from JPack.console import CmdLine
from JPack.args import jruntest_args
from JPack.print_args import jruntest_print_args

__version__ = "1.0.0.0"

def main():
    if len(argv) == 1:
        runtest() 
        return

    argv.remove(argv[0])

    for arg in argv:
        if jruntest_args.help(arg):
            jruntest_print_args.help()
            return
        elif jruntest_args.version(arg):
            jruntest_print_args.version(__version__)
            return
        elif jruntest_args.test_file(arg):
            runtest()

def runtest():
    __start__ = time()

    wd = getcwd()
    cfiles = listdir(wd)

    if not cfiles.__contains__("test.class"):
        print("test.class does not exist")
        if cfiles.__contains__("test.java"):
            print("run jcompile test.java or jcompile all")

    CmdLine(wd).run("test")
    print("Test completed")
    print(f"Time elapsed: {(time() - __start__):.2f}")

if __name__ == "__main__":
    main()