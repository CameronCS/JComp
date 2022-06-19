# JComp Documentation

## Introduction to JComp
JComp is the main file in this repository. It allows for app creation file and directory additions with standard boilerplate code

## Table of contents
[Help](#help)

[Version](#version)

[Create Java App](#create-java-app)

[Add File](#add-file)

[Add Dir](#add-dir)

[Add Files](#add-files)

[Add Dirs](#add-dirs)

## Help

The help command will currently list all arguments

The help command can be called one of two ways `-h` or `--help`

```
jcomp -h
```
or 
```
jcomp --help
```

## Version

The version command will return the current version of jcomp

The help command can be called one of two ways `-v` or `--version`

```
jcomp -v
```
or 
```
jcomp --version
```

## Create Java App
The JComp command `create-java-app` requires at least one additional argument `App Name` 

If the App name is left blank it will default to "my-java-app"

General JComp arguments. 
With the filename only
```
jcomp create-java-app MyApp
```
Will create the following directory
```
MyApp
| - Main.java
| - App.java
| - test.java
```
When creating a Java app you can add directories and files within the creation of the app.

The additional files do not have to be java files and you are required to specifiy the file extention.

When you don't specify the file extention the file is considered a folder
```
jcomp create-java-app MyApp Users Users/demo.txt External-Package External-Package/ExternClass.java
```
This creates the directory
```
MyApp
| - Users
  | - demo.txt
| - External-Package
  | - ExternClass.java
| - Main.java
| - App.java
| - test.java
```

Note: When adding directories and files the directories must be declared in the arguments before the "dir/file"

```
jcomp create-java-app MyApp Users/demo.txt Users
```
This line will create an error and fail the creation of the app.

## Add File
The `add-file` argument will add a file to the directory or a folders directory
```
jcomp add-file myFile.txt
```
Will generate a textfile in the current working directory

If the current working directory is the mainfile with the "Main.java" file. You can the use the "`/`" or "`\`" keys to specifiy the file
```
jcomp add-file Users/myFile.txt
```
This will then create a file in the "Users" folder in the main directory
## Add Dir
The `add-dir` command will add a new directory in the current file directory. 
```
jcomp add-dir MyNewDir
```
This command will add "MyNewDir" in the current working directory

If you add an extention the folder will be made with the file extention however it will be a folder

## Add Files
The `add-files` command allows you too add multiple files to a directory.

The file can be embedded in a another folder

```
jcomp add-files myFile1.txt  Users/UserFile.txt
```
Provided that the folder "Users" is a folder in the current working directory, The file `myFile.txt` will be created in the working directory and the `UserFile.txt` will be created in the "Users" folder in the working directory

## Add Dirs
The `add-dirs` command will add multiple folders in the current working directory
```
jcomp add-dirs Folder1 Folder2 Folder3
```
This will create the 3 current folders in the current working directory.
If the origional Folder was 
```
MyApp
| - Main.java
| - App.java
| - test.java
```
After running the previous command the directory will look like:
```
MyApp 
| - Folder1
| - Folder2
| - Folder3
| - Main.java
| - App.java
| - test.java
```

## Final Thoughts
There are many more functional commands to be added that will initilise projects with boiler plate code.
There are commands and functions yet to be added but community feedback will be greatly appreciated
