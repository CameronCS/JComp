# JCompile Documentation

## Introduction

## Table of Contents
[Help](#help)

[Version](#version)

[All](#all)

[File](#file)

## Help
The help commands currenly list all the arguments of the jcompile system

There are one of two ways to call the help command `-h` or `--help`
```
jcompile -h
```
or
```
jcompile --help
```

## Version
The version command will return the version of the jcompile

There are one of two ways to call the version of jcompile `-v` or `--version`
```
jcompile -v
```
or
```
jcompile --version
```

## All
The all command will compile all Java scripts in the current working directory and all files in additional folders in the current directory
```
jcompile all
```
This command will generate all the ".class" files in the directory and all embeded files

## File
The file command will compile a specific file. 
```
jcompile [filename].java
```
This command will compile that specific file and any other file related to that specific file. 

This allows for all compiling files specific files. And all possible files realted.

## Final Thoughts
There are still minor flaws to the jcompile system. There also command updates and other commands to be added to the jcompile system.
