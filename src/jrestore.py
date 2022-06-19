from os import getcwd, listdir, remove
from pickle import FALSE
from sys import argv
from time import time
from JPack.file_sys import get_embeded_dirs
from JPack.args import jrestore_args
from JPack.print_args import default, jrestore_print_args

__version__ = "1.0.0.0"

def main():
    if len(argv) == 1:
        print(default.NO_ARG)
        return

    _self = argv.pop(0)

    if (jrestore_args.files(argv)):
        files(argv)
        return

    for arg in argv:
        if jrestore_args.help(arg):
            jrestore_print_args.help()
            return
        elif jrestore_args.version(arg):
            jrestore_print_args.version(__version__)
        elif jrestore_args.all(arg):
            full_back_up()
            return
        elif jrestore_args.file(arg):
            file_back_up(arg, False)
            return
        else:
            print(f"{_self} - Argument invalid: {arg}")
            return

def full_back_up():
    __start__ = time()

    while True:
        print("Are you sure you want to restore ALL of the java files?")
        inp = input("(y/n): ")
        if inp.casefold() == "y":
            break
        elif inp.casefold() == "n":
            print("Restoration cancelled")
            return
        else:
            print("Command invalid")
    wd = getcwd()

    check = listdir(wd)
    jcheck = [item for item in check if item.endswith(".java")]

    if jcheck.__contains__("Main.java") is False:
        print("Please use this command in the directory that contains the 'Main.java' file")
        return

    embededfiles = get_embeded_dirs(wd)


    bdirs = []
    for file in embededfiles:
        if file.endswith("backups"):
            bdirs.append(file)

    for bdir in bdirs:
        bfiles = listdir(bdir)

        file_content = []
        all_content = {}
        for bfile in bfiles:
            print(bfile)
            with open(f"{bdir}\\{bfile}", 'r') as f:
                file_content = f.readlines()
                f.close()
                
            all_content[bfile] = file_content

            rootdir = str(bdir).removesuffix("\\backups")
            _jfiles = listdir(rootdir)
            jfiles = [jfile for jfile in _jfiles if jfile.endswith(".java")]

        for jfile in jfiles:
            with open(f"{rootdir}\\{jfile}", 'w') as f:
                f.writelines(all_content[f"{jfile}.backup"])
                f.close()

    print("A full restoration has been completed")
    print(f"Time elapsed: {(time() - __start__):.2f}")

def file_back_up(arg: str, files: bool):
    if files is False:
        __start__ = time()
        
    try:
        remove(arg)
    except FileNotFoundError:
        print(f"File {arg} not found")
        return

    _files = listdir("./backups")
    file = None

    for _file in _files:
        if _file == f"{arg}.backup":
            file = _file

    if file is None:
        print("Backup file does not exist")
        return

    lines = []
    with open(f"./backups/{arg}.backup", 'r') as f:
        lines = f.readlines()
        f.close()

    with open(arg, 'x') as f:
        f.writelines(lines)
        f.close()

    print(f"File: {arg} has been restored")
    if files is False:
        print(f"Elapsed time: {(time() - __start__):.2f}")

def files(files: list[str]):
    __start__ = time()
    for file in files:
        file_back_up(file, True)

    print("Files restored")
    print(f"Time elapsed: {(time() - __start__):.2f}")

if __name__ == "__main__":
    main()