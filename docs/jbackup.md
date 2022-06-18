# JBackup Documentation

## Introduction
The jbackup system is a simple way to create local backups of your java files

the term "local" is being used currently as the external factor is being developed as you are reading this 

## Table of contents

[1: Help](#help)

[2: Version](#version)

[3: All](#all)

[4: A specific file](#a-specific-file)

## Help

Help command currently only lists arguments.

There are 2 ways to call the help argument
```-h``` or ```--help```

It is run simply in the terminal as:
```
jbackup -h
```
or 
``` 
jbackup --help
```


## Version

The version command will return the current version of the jbackup system.

The 2 ways to call the version argument are
```-v``` or ```--version```

These commands are simply run in the terminal like:
```
jbackup -v
```
or
```
jbackup --version
```

## All

The all argument in used to create a local backup of all existing files.
```j
backup all
``` 
will walk through all java files in the root directory and create backups of them.

Note '.jav' files currently are not included but will be soon

## A Specific file
Currently in development a person can only backup one specific file using the the specific file argument. 

There is nothing special about it its just the ```[filename].java```

No need for a keyword here. It will find the filename and back it up in the respective section
```
jbackup Main.java
```

## Final Remarks
Please keep in mind the entire JComp system is currently still in development and anything here is the very first and primitive release. 
