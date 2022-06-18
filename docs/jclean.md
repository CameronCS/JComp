# JClean documentation

## Introduction
JClean is the section of the Java Compiler System that removes any and all ".class" files in the current directory

## Table of contents
[1: Help](#help)

[2: Version](#version)

[3: All](#all)

[4: Files](#files)

## Help
The help command will currenly only list avaliable arguments.

The help command is called one of two wats ```-h``` or ```--help```

```
jclean -h
```
or
```
jclean --help
```

## Version
The version command will return the version of the jclean system

The version command is called one of two ways ```-v``` or ```--version```

```
jclean -v
```
or
```j
clean --version
```

## All
The all command will clean any and all ".class" files in the files directory

```
jclean all
```

## Files
To remove specific files your file will end with the ```[filename].class``` these class files will will be removed and be cleaned from the directory
```
jclean Main.class
```
This command will remove the the "Main.class" file from the current working directory


## Final Thoughts
The JClean system is still in development and  requires community feedback
