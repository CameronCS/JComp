from typing import Final, final

__package__ = "JPack"
__version__ = "1.1.0.0"
__name__    = "args.py"
__all__     = ["jcomp_args", "jbackup_args", "jcompile_args", "jclean_args"]

"""
===========
===JCOMP===
===========

These are the arguments
for the jcomp file system
and are to be used as 
static methods
"""
class jcomp_args:
    @final
    @staticmethod
    def equHelp(arg: str) -> bool:
        return arg == "-h" or arg == "--help"
    @final
    @staticmethod
    def equVer(arg: str) -> bool:
        return arg == "-v" or arg == "--version"
    @final
    @staticmethod
    def equCJA(arg: str) -> bool:
        return arg == "create-java-app"
    @final
    @staticmethod
    def equAF(arg: str) -> bool:
        return arg == "add-file"
    @final
    @staticmethod
    def equAD(arg: str) -> bool:
        return arg == "add-dir"
    @final
    @staticmethod
    def equAFS(arg: str) -> bool:
        return arg == "add-files"
    @final
    @staticmethod
    def equADS(arg: str) -> bool:
        return arg == "add-dirs"

"""
=============
===JBACKUP===
=============

These are the arguments
for the jbackup file system
and are to be used as 
static methods
"""
class jbackup_args:
    @final
    @staticmethod
    def equAll(arg: str) -> bool:
        return arg == "all"
    @final
    @staticmethod 
    def equHelp(arg: str) -> bool:
        return arg == "-h" or arg == "--help"
    @final
    @staticmethod
    def equVersion(arg: str) -> bool:
        return arg == "-v" or arg == "--version"
    @final
    @staticmethod
    def isJava(arg: str) -> bool:
        return arg.endswith(".java")

"""
==============
===JCOMPILE===
==============

These are the arguments
for the jcompile file system
and are to be used as 
static methods
"""
class jcompile_args:
    @final
    @staticmethod
    def help(arg: str) -> bool:
        return arg == "-h" or arg == "--help"
    @final
    @staticmethod
    def version(arg: str) -> bool:
        return  arg == "-v" or arg == "--version"
    @final
    @staticmethod
    def all(arg: str) -> bool:
        return arg == "all"
    @final
    @staticmethod
    def equFile(arg: str) -> bool:
        return arg.endswith(".java")
"""
==============
===JCOMPILE===
==============

These are the arguments
for the jcompile file system
and are to be used as 
static methods
"""
class jclean_args:
    @final 
    @staticmethod
    def help(arg: str) -> bool:
        return arg == "-h" or arg == "--help"
    @final
    @staticmethod
    def version(arg: str) -> bool:
        return arg == "-v" or arg == "--version"
    @final
    @staticmethod
    def equAll(arg: str) -> bool:
        return arg == "all"
    @final 
    @staticmethod
    def equfile(arg: str) -> bool:
        return arg.endswith(".class")

"""
==============
===JRESTORE===
==============

These are the arguments
for the jrestore file system
and are to be used as 
static methods
"""
class jrestore_args:
    @final
    @staticmethod
    def help(arg: str) -> bool:
        return arg == "-h" or arg == "--help"
    
    @final
    @staticmethod
    def version(arg: str) -> bool:
        return arg == "-v" or arg == "--version"

    @final
    @staticmethod
    def files(argv: list[str]):
        return len(argv) > 1

    @final
    @staticmethod
    def file(arg: str) -> bool:
        return arg.endswith(".java")

    @final
    @staticmethod
    def all(arg: str) -> bool:
        return arg == "all"

"""
==========
===JRUN===
==========

These are the arguments
for the jrun file system
and are to be used as 
static methods
"""

class jrun_args:
    @final
    @staticmethod
    def help(arg: str) -> bool:
        return arg == "-h" or arg == "--help"

    @final 
    @staticmethod
    def version(arg: str) -> bool:
        return arg == "-v" or arg == "--version"

    @final
    @staticmethod
    def mainfile(arg: str) -> bool:
        return arg == "Main"

"""
==============
===JRESTORE===
==============

These are the arguments
for the jrestore file system
and are to be used as 
static methods
"""
class jruntest_args:
    @final
    @staticmethod
    def help(arg: str):
        return arg == "-h" or arg == "--help"

    @final
    @staticmethod
    def version(arg: str):
        return arg == "-v" or arg == "--version"

    @final
    @staticmethod
    def test_file(arg: str):
        return arg == "test"