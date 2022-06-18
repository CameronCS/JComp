from os import mkdir, getcwd
from time import time
from JPack.jfile_content import generate_app, generate_file, generate_main, generate_test
from JPack.file_sys import get_file, get_folder

__package__ = "JPack"
__version__ = "1.1.0.0"
__name__    = "create_java_app.py"
__all__     = ["make", "makefile", "makefiles", "makedir", "makedirs"]

def make(args: list[str]):
    __START__ = time()
    jfiles    = ["Main.java", "App.java", "Test.java"]
    folders   = ["backups"]
    dir       = getcwd()
    name      = args[0]
    args.remove(args[0])

    try:
        mkdir(f"{dir}\\{name}")
    except FileExistsError:
        print(f"The Appname {name} is invalid")
        print(f"A folder {name} already exists")
        print("App creation failed")
        return

    print(f"Dir: {dir}\\{name} created")

    for arg in args:
        if jfiles.__contains__(arg):
            print(f"File: {arg} already created")
            print("Skippiing file")
            continue
        elif arg.__contains__("."):jfiles.append(arg)
        else:                      folders.append(arg)

    _makedirs(dir, name, folders)
    _makefiles(dir, name, jfiles)
    make_backups(dir, name, jfiles)

    print(f"Java App Created")
    print(f"Time elapses: {(time() - __START__):.2f}")

    print("\n")
    print("Command 'jrun' will automatically the main file")
    print("Command 'jruntest' will run the test file")
    print("Command 'jcompile all' will compile all java files into the class files")
    print("Command 'jclean all' will remove all .class files from the current directory")

def _makedirs(path: str, appName: str, folders: list[str]):
    for folder in folders:
        mkdir(f"{path}\\{appName}\\{folder}")
        print(f"Dir: {path}\\{appName}\\{folder} created")

def _makefiles(path: str, name: str, jfiles: list[str]):
    for jfile in jfiles:
        created = False
        file = f"{path}\\{name}\\{jfile}"
        if jfile == "Main.java":
            with open(file, 'x') as f:
                f.writelines(generate_main())
                f.close()
                created = True
        elif jfile == "App.java":
            with open(file, 'x') as f:
                f.writelines(generate_app())
                f.close()
                created = True
        elif jfile == "Test.java":
            with open(file, 'x') as f:
                f.writelines(generate_test())
                f.close()
                created = True
        elif jfile.endswith(".java"):
            try:
                with open(file, 'x') as f:
                    f.writelines(generate_file(jfile))
                    f.close()
            except ValueError:
                    print(f"{jfile} could not be created to a naming error")
                    print(f"This will not stop the rest of the files from")
                    print(f"being created")
            except FileExistsError:
                print(f"The file \"{jfile}\" already exists")
            except FileNotFoundError:
                if jfile.__contains__("\\") or jfile.__contains__("/"):
                    _folder = get_folder(jfile)
                    print(f"Folder: {_folder} does not exist")
                    print(f"This file will be skipped")
        else:
            try:
                with open(file, 'x') as f:
                    f.close()
            except ValueError:
                    print(f"{jfile} could not be created to a naming error")
                    print(f"This will not stop the rest of the files from")
                    print(f"being created")
            except FileExistsError:
                print(f"The file \"{jfile}\" already exists")
            except FileNotFoundError:
                if jfile.__contains__("/") or jfile.__contains__("\\"):
                    jfolder = get_folder(jfile)
                    print(f"Folder: {jfolder} can not be found")
                    print(f"File: {jfile} will be skipped")

        if created:
            print(f"File created: {jfile}")

def make_backups(path: str, name: str, jfiles: list[str]):
    for jfile in jfiles:
        created = False
        lines   = list[str]
        with open(f"{path}\\{name}\\{jfile}", 'r') as f:
            lines = f.readlines()
            f.close()

        if (jfile.__contains__("/") or jfile.__contains__("\\")) and jfile.endswith(".java"):
            folder = get_folder(jfile)
            file   = f"{get_file(jfile)}.backup"

            try:
                mkdir(f"{path}\\{name}\\{folder}\\backups")
            except FileExistsError:
                continue

            with open(f"{path}\\{name}\\{folder}\\backups\\{file}", 'x') as f:
                f.writelines(lines)
                f.close()
                created = True
        elif jfile.endswith(".java"):
            with open(f"{path}\\{name}\\backups\\{jfile}.backup", 'x') as f:
                f.writelines(lines)
                f.close()
                created = True
        if created is True:
            print(f"Backup created: {jfile}.backup")

def makefile(filename: str):
    path    = getcwd()
    created = False 
    isjava  = filename.endswith(".java")
    
    try:
        with open(f"{path}\\{filename}", 'x') as f:
            if isjava is True:
                f.writelines(generate_file(filename))
            created = True
            f.close()
    except ValueError:
        print(f"{filename} could not be created to a naming error")
        print(f"This will not stop the rest of the files from")
        print(f"being created")
    except FileExistsError:
        print(f"The file \"{filename}\" already exists")
        print(f"This file will be skipped")
    except FileNotFoundError:
        if filename.__contains__("/") or filename.__contains__("\\"):
            folder = get_folder(filename)
            print(f"Folder: {folder} was not found")
            print(f"The file {filename} will be skipped")

    if created is True and isjava is True:
        lines = list[str]

        with open(f"{path}\\{filename}", "r") as f:
            lines = f.readlines()
            f.close()

        folder = f"\\{get_folder(filename)}" if filename.__contains__("/") or filename.__contains__("\\") else ""

        if folder != "":
            file = get_file(filename)
            try:
                mkdir(f"{path}{folder}\\backups")
            except FileExistsError:
                pass
        else:
            file = filename

        with open(f"{path}{folder}\\backups\\{file}.backup", 'x') as f:
            f.writelines(lines)
            f.close()

    if created is True:
        print(f"File Created: {filename}")
        print(f"Backupfile created: {folder}\\{file}.backup")

def makefiles(files: list[str]):
    path = getcwd()
    for file in files:
        created = False
        try:
            with open(f"{path}\\{file}", 'x') as f:
                created = True
                if file.endswith(".java"):
                    f.writelines(generate_file(file))
                f.close()
        except ValueError:
            print(f"{file} could not be created to a naming error")
            print(f"This will not stop the rest of the files from")
            print(f"being created")
        except FileExistsError:
            print(f"The file \"{file}\" already exists")

        if created is True:
            lines = []
            with open(f"{path}\\{file}", 'r') as f:
                lines = f.readlines()
                f.close()

            folder = f"\\{get_folder(file)}" if file.__contains__("/") or file.__contains__("\\") else ""

            if folder != "":
                file = get_file(file)
                try:
                    mkdir(f"{path}{folder}\\backups")
                except FileExistsError:
                    pass

            with open(f"{path}{folder}\\backups\\{file}.backup", 'x') as f:
                f.writelines(lines)
                f.close()

            print(f"File created: {folder}\\{file}")
            print(f"Backupfile created: {folder}\\backups\\{file}.backup")

def makedir(dir: str):
    path = getcwd()

    try:
        mkdir(f"{path}\\{dir}")
    except(FileExistsError):
        print("Directory already exists")
        return

    print(f"sucessfully created: {path}\\{dir}")

def makedirs(dirs: list[str]):
    for _dir in dirs:
        path = getcwd()

        try:
            mkdir(f"{path}\\{_dir}")
        except(FileExistsError):
            print(f"Directory {_dir} already exists")
            print("This does not effect the creation of other directories")

        print(f"created: {path}\\{_dir}")