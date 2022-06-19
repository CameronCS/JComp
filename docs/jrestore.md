# JRestore Documentation

## Introduction

Currently the JRestore function reverts changes from the local backup files in the backups directory

## Table of Contents

[Help](#help)

[Version](#version)

[All](#all)

[File](#files)

## Help
The help command currently lists all arguments in the jrestore functions

Help arguments are called one of two ways `-h` or `--help`
```
jrestore -h
```
or
```
jrestore --help
```

## Version
The version commands list the version of the JRestore

JRestore version commands are called one of two ways `-v` or `--version`

```
jrestore -v
```
or 
```
jrestore --version
```

## All
The all command will ask the you for a final conformation a yes or a no. If you say yes, and regret it, I am very sorry.

The command line is really simple
```
jrestore all
```
There will be the following message
```
Are you sure you want to restore ALL of the java files?
(y/n):
```
And thats it. If you say yes all your files will be restored

If you say no then jrestore ends its execution there

If any other argument is put in, jrestore will no read it and prompt you again.

## File
You can also user jrestore on stand alone files.

```
jrestore myFile.java
```
jrestore will replace the file with the backup file. If the backup file exists of course.


## Final thoughts
JRestore is still undergoing development and any community feedback will be greatly appreciated!
