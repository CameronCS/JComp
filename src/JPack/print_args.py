from typing import final

__package__ = "JPack"
__version__ = "1.1.0.0"
__name__    = "print_args.py"
__all__     = [
    "default",
    "jcomp_help_args",
    "jbackup_help_args",
    "jcompile_help_args",
    "jclean_help_args"
]
"""
===========
==default==
===========
"""
class default:
    NO_ARG = "type '-h' or '--help' for all the args the all the args"

class jcomp_print_args:
    @final
    @staticmethod
    def help() -> None:
        print(
            "-v or --version for the version of the jcomp\n",
            "create-java-app [name] to create a java app with Main Test App .java files\n",
            "add-file [name_of_file] to add a file with a code skeleton\n",
            "add-dir [dir name] will create a directory within the current working directory\n",
            "add-files list[files] adds multiple files in the directorty\n",
            "add-dirs list[dirs] adds multiple directories in the directory\n"
        )
    @final
    @staticmethod
    def version(version: str) -> str:
        print(f"jcomp version: {version}")
"""
===========
==jbackup==
===========
"""
class jbackup_print_args:
    @final
    @staticmethod
    def help() -> None:
        print(
            "-v or --version for the version of the app\n",
            "all to backup all files in the directory\n",
            "filename.java to backup that specific file\n"
        )
    @final
    @staticmethod
    def version (version: str):
        print(f"jbackup version: {version}")

"""
============
==jcompile==
============
"""
class jcompile_print_args:
    @final
    @staticmethod
    def help():
        print(
            "-v or --version for the version of jcompile\n",
            "all to compile all the files in the directory\n"
            "[filename.java] for that specific file and all related files\n"
        )
    @final
    @staticmethod
    def version(version: str):
        print(f"jcompile version: {version}")
"""
==========
==jclean==
==========
"""
class jclean_print_args:
    @final
    @staticmethod
    def help():
        print(
            "-v or --version for the version of jclean\n",
            "all to clean all .class files\n",
            "[list] to remove a list of .class files\n",
            "the .class extention does not need to be specified\n"
        )
    @final
    @staticmethod
    def version(version: str):
        print(f"jclean version: {version}")

"""
============
==jrestore==
============
"""
class jrestore_print_args:
    @final
    @staticmethod
    def help():
        print(
            "-v or --version for the version\n",
            "all to restore all files in directory\n",
            "[filename].java to restore that file\n",
            "multiple files to restore multiple files\n"
        )

    @final
    @staticmethod
    def version(version: str):
        print(f"jrestore version: {version}")


"""
========
==jrun==
=========
"""
class jrun_print_args:
    def help():
        print(
            "-v or --version for the files version\n",
            "Main to run the main class file\n",
            "[filename] to run a filename\n"
            "provide no arguments to look for the 'Main.class' file\n"
        )

    def version(version):
        print(f"jrun version: {version}")


"""
============
==jruntest==
============
"""  
class jruntest_print_args:
    def help():
        print(
            "-v or --version for the files version"
        )
    
    def version(version: str):
        print(f"jruntest version: {version}")