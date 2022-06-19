from sys import argv
from os import getcwd, listdir, mkdir
from time import time
from JPack.print_args import default, jbackup_print_args
from JPack.args import jbackup_args

__version__ = "1.1.0.0"

def main():
    global __START__
    
    __START__ = time()

    if len(argv) == 1:
        print(default.NO_ARG)


    _self = argv.pop(0)

    for arg in argv:
        if jbackup_args.equAll(arg):
            all()
            return
        elif jbackup_args.isJava(arg):
            backup_file(arg)
            return
        elif jbackup_args.equHelp(arg):
            jbackup_print_args.help()
            return
        elif jbackup_args.equVersion(arg):
            jbackup_print_args.version(__version__)
            return
        else:
            print(f"{_self} - Invalid argument: {arg}")

def all():
    wd = getcwd()
    ls = listdir(wd)

    jfiles = [lsi for lsi in ls if lsi.endswith(".java")]
    for jfile in jfiles: ls.remove(jfile)
    folders = ls

    if len(jfiles) == 0:
        print("No java files found")
        return

    ls = None

    for jfile in jfiles:
        lines = []
        with open(f"{wd}\\{jfile}", 'r') as f:
            lines = f.readlines()
            f.close()
        try:
            with open(f"{wd}\\backups\\{jfile}.backup", 'x') as f:
                f.writelines(lines)
                f.close()
        except FileExistsError:
            with open(f"{wd}\\backups\\{jfile}.backup", 'w') as f:
                f.writelines(lines)
                f.close()

        print(f"File backed up: {jfile}")
    for folder in folders:
        nwd = f"{wd}\\{folder}"
        ls = listdir(nwd)
        for jfile in ls:
            if jfile.endswith(".java"):
                lines = []
                with open(f"{nwd}\\{jfile}", 'r') as f:
                    lines = f.readlines()
                    f.close()
                try: 
                    mkdir(f"{nwd}\\backups")
                except FileExistsError:
                    pass
                try:
                    with open(f"{nwd}\\backups\\{jfile}.backup", 'x') as f:
                        f.writelines(lines)
                        f.close()
                except FileExistsError:
                    with open(f"{nwd}\\backups\\{jfile}.backup", 'w') as f:
                        f.writelines(lines)
                        f.close()
                print(f"File backed up: {folder}\\{jfile}")
    print(f"Time elapsed: {(time() - __START__):.2f}")

def backup_file(arg: str):
    wd = getcwd()
    ls = listdir(wd)
    fnfe = False

    jfiles = [item for item in ls if item.endswith(".java")]
    for jfile in jfiles: ls.remove(jfile)

    if len(jfiles) == 0:
        print(f"File: {arg} was not found")
        return

    if arg in jfiles:
        lines = []
        with open(f"{wd}\\{arg}", 'r') as f:
            lines = f.readlines()
            f.close()

        try:
            mkdir(f"{wd}\\backups")
        except FileExistsError:
            pass

        try:
            with open(f"{wd}\\backups\\{arg}.backup", 'x') as f:
                f.writelines(lines)
                f.close
        except FileExistsError:
            with open(f"{wd}\\backups\\{arg}.backup", 'w') as f:
                f.writelines(lines)
                f.close()
        print(f"File backed up: {arg}")
    else:
        folders = ls
        ls      = 0x000000
        found   = False
        while found is False and fnfe == False:
            for folder in folders:
                nwd = f"{wd}\\{folder}"
                ls  = listdir(nwd)

                if arg in ls:
                    found = True
                    lines = []
                    with open(f"{nwd}\\{arg}", 'r') as f:
                        lines = f.readlines()
                        f.close()

                    try:
                        mkdir(f"{nwd}\\backups")
                    except FileExistsError:
                        pass
                    
                    try:
                        with open(f"{nwd}\\backups\\{arg}.backup", "x") as f:
                            f.writelines(lines)
                            f.close()
                    except FileExistsError:
                        with open(f"{nwd}\\backups\\{arg}.backup", "w") as f:
                            f.writelines(lines)
                            f.close()

                    print(f"File backed up: {folder}\\{arg}")
                
                if folder == folders[len(folders) - 1] and found is False:
                    fnfe = True

    if fnfe is True:
        print(f"The file: {arg} was not found")

    print(f"Time elapsed: {(time() - __START__):.2f}")

if __name__ == "__main__":
    main()