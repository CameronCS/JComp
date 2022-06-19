# JRun Documentation

## Introduction
JRun is a simple way to run your java programs after you've you've compiled them. Using `jcompile all ` of course ;).
There are no arguments required but there are arguments you can pass. And there will be more to come!

## Table of Contents
[No Arg](#no-arg)

[Help](#help)

[Version](#version)

[Main](#main)

[File](#file)

## No Arg
As said in the Introduction there are no arguments required to use jrun.
If you wish not to use arguments jrun will automatically look for the 'main.class' file
```
jrun
````
Thats it. Your java Application will run

## Help
The help command will list all possible arguments to run. 

Help arguments are called one of two ways `-h` or `--help`
```
jrun -h
```
or
```
jrun --help
```

## Version
The version command will return the version of jrun

The Version argument is called one of two ways `-v` or `--version`
```
jrun -v
```
or
```
jrun --version
```

## Main
When selecting the `Main.class` file jrun will look for it and run it if it is found.

This is however not required but can be used to specifiy that the `Main.class` file is the file you wish to execute
```
jrun Main
```

## File
The `[filename]` argument is just incase you want to run the application using a seperate file. 
This will allow for the separate file to be run.
```
jrun debug_app.class
```

## Final Thoughts
JRun is still a work in progress and any community feedback will be highly appreciated!
